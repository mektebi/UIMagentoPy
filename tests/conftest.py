"""
This module contains shared fixtures.
"""

import json
import selenium.webdriver
import pytest
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

global driver

@pytest.fixture(scope='session', autouse=True)
def config():

  # Read the file
  with open('config.json') as config_file:
    config = json.load(config_file)
  
  # Assert values are acceptable
  assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome', 'Safari', 'internet explorer']
  assert isinstance(config['implicit_wait'], int)
  assert config['implicit_wait'] > 0

  # Return config so it can be used
  return config


@pytest.fixture(scope='session', autouse=True)
def browser():

  with open('config.json') as config_file:
    config = json.load(config_file)

  global driver



  if config['browser'] == 'Firefox':
    driver = selenium.webdriver.Firefox()
  elif config['browser'] == 'Chrome':
    driver = selenium.webdriver.Chrome()
    # driver = selenium.webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME)
  elif config['browser'] == 'Safari':
    driver = selenium.webdriver.Safari()
  elif config['browser'] == 'Headless Chrome':
    opts = selenium.webdriver.ChromeOptions()
    opts.add_argument('headless')
    driver = selenium.webdriver.Chrome(options=opts)



  # Make its calls wait for elements to appear
  driver.implicitly_wait(config['implicit_wait'])

  # Return the WebDriver instance for the setup
  yield driver

  # Quit the WebDriver instance for the cleanup
  driver.quit()
  return driver



@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
  """`
  Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
  :param item:
  """
  pytest_html = item.config.pluginmanager.getplugin('html')
  outcome = yield
  report = outcome.get_result()
  extra = getattr(report, 'extra', [])

  if report.when == 'call' or report.when == "setup":
    xfail = hasattr(report, 'wasxfail')
    if (report.skipped and xfail) or (report.failed and not xfail):
      file_name = report.nodeid.replace("::", "_")+".png"
      _capture_screenshot(file_name)
      if file_name:
        html = '<div><img src="%s" alt="screenshot" style="width:600px;height:228px;" ' \
               'onclick="window.open(this.src)" align="right"/></div>'%file_name
        extra.append(pytest_html.extras.html(html))
    report.extra = extra


def _capture_screenshot(name):
  global driver
  driver.get_screenshot_as_file(name)

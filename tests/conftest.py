"""
This module contains shared fixtures.
"""

import json
import pytest
from datetime import datetime
import selenium.webdriver
import pytest
driver = None

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
def browser(config):

  global driver
  # if driver is None:
  #   driver = webdriver.Chrome()
  # Initialize the WebDriver instance

  if config['browser'] == 'Firefox':
    driver = selenium.webdriver.Firefox()
  elif config['browser'] == 'Chrome':
    driver = selenium.webdriver.Chrome()
  elif config['browser'] == 'Safari':
    driver = selenium.webdriver.Safari()
  elif config['browser'] == 'Internet Explorer':
    driver = selenium.webdriver.ie();
  elif config['browser'] == 'Headless Chrome':
    opts = selenium.webdriver.ChromeOptions()
    opts.add_argument('headless')
    driver = selenium.webdriver.Chrome(options=opts)
  else:
    raise Exception(f'Browser "{config["browser"]}" is not supported')


  # Make its calls wait for elements to appear
  driver.implicitly_wait(config['implicit_wait'])

  # Return the WebDriver instance for the setup
  yield driver

  # Quit the WebDriver instance for the cleanup
  driver.quit()
  return driver

# @pytest.fixture(scope='session', autouse=True)
# def browser():
#   global driver
#   if driver is None:
#     driver = webdriver.Chrome()
#   yield driver
#   driver.quit()
#   return driver


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
  driver.get_screenshot_as_file(name)

# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item, call):
#   pytest_html = item.config.pluginmanager.getplugin('html')
#   outcome = yield
#   report = outcome.get_result()
#   extra = getattr(report, 'extra', [])
#   driver = browser;
#   summary = []
#   if report.when == 'call':
#       # always add url to report
#       extra.append(pytest_html.extras.url('http://www.example.com/'))
#       _gather_screenshot(item, report, driver, summary, extra)
#       # extra.append(pytest_html.extras.image("screenshot-2020-06-07_16-57-24.png", mime_type='image/png', extension='png'))
#       xfail = hasattr(report, 'wasxfail')
#       if (report.skipped and xfail) or (report.failed and not xfail):
#         # only add additional html on failure
#         extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
#       report.extra = extra
#
# def _gather_screenshot(item, report, driver, summary, extra):
#   screenshot = driver.get_screenshot_as_base64()
#   pytest_html = item.config.pluginmanager.getplugin('html')
#   if pytest_html is not None:
#     # add screenshot to the html report
#     extra.append(pytest_html.extras.image(screenshot, 'Screenshot'))
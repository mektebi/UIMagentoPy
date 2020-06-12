"""
This module contains AccountPage,
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class AccountPage:

  # Locators

  PAGE_MESSAGE = (By.XPATH, '//*[@id="maincontent"]/div[1]/div[2]/div/div/div')
  BOX_CONTENT = (By.XPATH, '//*[@id="maincontent"]/div[2]/div[1]/div[3]/div[2]/div[1]/div[1]')

  # Initializer

  def __init__(self, browser):
    self.browser = browser

  # Interaction Methods

  def message(self):
    page_message = self.browser.find_element(*self.PAGE_MESSAGE)
    return page_message.text

  def box_content(self):
    content = self.browser.find_element(*self.BOX_CONTENT)
    return content.text



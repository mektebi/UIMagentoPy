"""
This module contains HomePage,
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class HomePage:

  # URL

  URL = 'https://m2.leanscale.com'

  # Locators

  SEARCH_INPUT = (By.ID, 'search')
  SEARCH_BUTTON = (By.ID, 'search')
  USER_CONTROLS = (By.XPATH, '/html/body/div[1]/header/div[1]/div/ul/li[2]')
  SIGNOUT_BUTTON = (By.XPATH, '/html/body/div[1]/header/div[1]/div/ul/li[2]/div/ul/li[3]')
  SIGNIN_BUTTON = (By.XPATH, '/html/body/div[1]/header/div[1]/div/ul/li[2]/a')
  SIGNOUT_MESSAGE = (By.XPATH, '//*[@id="maincontent"]/div[1]/h1/span')

  # Initializer

  def __init__(self, browser):
    self.browser = browser

  # Interaction Methods

  def load(self):
    self.browser.get(self.URL)

  def search(self, phrase):
    search_input = self.browser.find_element(*self.SEARCH_INPUT)
    search_input.send_keys(phrase, Keys.ENTER)

  def logout(self):
    self.browser.find_element(*self.USER_CONTROLS).click()
    self.browser.find_element(*self.SIGNOUT_BUTTON).click()

  def go_to_login_page(self):
    self.browser.find_element(*self.SIGNIN_BUTTON).click()


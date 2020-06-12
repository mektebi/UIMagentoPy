"""
This module contains LoginPage,
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class LoginPage:

  # URL


  # Locators

  EMAIL_INPUT = (By.ID, 'email')
  PASSWORD_INPUT = (By.ID, 'pass')
  SIGNIN_BUTTON = (By.ID, 'send2')

  # Initializer

  def __init__(self, browser):
    self.browser = browser

  # Interaction Methods

  def load(self):
    self.browser.get(self)

  def login(self, email, password):
    email_input = self.browser.find_element(*self.EMAIL_INPUT)
    email_input.send_keys(email)
    password_input = self.browser.find_element(*self.PASSWORD_INPUT)
    password_input.send_keys(password)
    self.browser.find_element(*self.SIGNIN_BUTTON).click()
"""
This module contains RegisterPage,
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import names

class RegisterPage:

  # URL

  URL = 'https://m2.leanscale.com/customer/account/create/'

  # Locators

  FIRSTNAME_INPUT = (By.ID, 'firstname')
  LASTNAME_INPUT = (By.ID, 'lastname')
  EMAIL_INPUT = (By.ID, 'email_address')
  PASSWORD_INPUT = (By.ID, 'password')
  CONFIRM_PASSWORD_INPUT = (By.ID, 'password-confirmation')
  CREATE_BUTTON = (By.XPATH, '//*[@id="form-validate"]/div/div[1]/button')
  ERROR_MESSAGE = (By.XPATH, '/html/body/div[1]/main/div[2]/div[2]/div/div/div')

  # Initializer

  def __init__(self, browser):
    self.browser = browser

  # Interaction Methods

  def load(self):
    self.browser.get(self.URL)

  def register(self, fname, lname, email, password, confirm_password):
    firstname_input = self.browser.find_element(*self.FIRSTNAME_INPUT)
    firstname_input.send_keys(fname)

    lastname_input = self.browser.find_element(*self.LASTNAME_INPUT)
    lastname_input.send_keys(lname)

    email_input = self.browser.find_element(*self.EMAIL_INPUT)
    email_input.send_keys(email)

    password_input = self.browser.find_element(*self.PASSWORD_INPUT)
    password_input.send_keys(password)

    password_confirmation_input = self.browser.find_element(*self.CONFIRM_PASSWORD_INPUT)
    password_confirmation_input.send_keys(confirm_password)

    create_button = self.browser.find_element(*self.CREATE_BUTTON)

    create_button.click()


  def error_message(self):
    message = self.browser.find_element(*self.ERROR_MESSAGE)
    return message.text
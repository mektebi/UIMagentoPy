
import pytest
from datetime import datetime
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from tests.Main_parameters import *


from pages.register import RegisterPage
from pages.account import AccountPage
from pages.home import HomePage

def test_false_register(browser):
  register_page = RegisterPage(browser)
  account_page = AccountPage(browser)

  data = MainParameter()
  email = 'roni_cost@example.com'

  # Given the register page is displayed
  register_page.load()

  register_page.register(data.namegenerator(), data.surnamegenerator(), email, 'LeanScale7', 'LeanScale7')

  WebDriverWait(browser, 30).until(EC.visibility_of_element_located(register_page.ERROR_MESSAGE))

  assert "There is already an account with this email address. If you are sure that it is your email address, click here to get your password and access your account." in register_page.error_message()


def test_positive_register(browser):
  register_page = RegisterPage(browser)
  account_page = AccountPage(browser)
  home_page = HomePage(browser)

  data = MainParameter()
  email = data.emailgenerator()

  # Given the register page is displayed
  register_page.load()

  register_page.register(data.namegenerator(), data.surnamegenerator(), email, 'LeanScale7', 'LeanScale7')

  WebDriverWait(browser, 30).until(EC.visibility_of_element_located(account_page.PAGE_MESSAGE))

  assert email in account_page.box_content()

  assert "Thank you for registering with Main Website Store." in account_page.message()

  home_page.logout()

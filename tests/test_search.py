

import pytest
from datetime import datetime
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from tests.Main_parameters import *


from pages.home import HomePage
from pages.search_result import SearchResultPage
from pages.login import LoginPage

def test_unlogged_register(browser):
    home_page = HomePage(browser)
    result_page = SearchResultPage(browser)

    # Given the home page is displayed
    home_page.load()


    WebDriverWait(browser, 30).until(EC.visibility_of_element_located(home_page.SIGNOUT_MESSAGE))

    home_page.search('Erika Running Short')

    WebDriverWait(browser, 30).until(EC.visibility_of_element_located(result_page.SIZE))

    result_page.add_to_cart()

    WebDriverWait(browser, 30).until(EC.visibility_of_element_located(result_page.PAGEMESSAGE))

    assert "You added Erika Running Short to your shopping cart." in result_page.success_message()




def test_logged_register(browser):
    home_page = HomePage(browser)
    result_page = SearchResultPage(browser)
    login_page = LoginPage(browser)

    # Given the home page is displayed
    home_page.load()

    home_page.go_to_login_page()

    WebDriverWait(browser, 30).until(EC.visibility_of_element_located(login_page.EMAIL_INPUT))

    login_page.login('roni_cost@example.com', 'roni_cost3@example.com')

    WebDriverWait(browser, 30).until(EC.visibility_of_element_located(home_page.SIGNOUT_MESSAGE))

    home_page.search('Erika Running Short')

    WebDriverWait(browser, 30).until(EC.visibility_of_element_located(result_page.SIZE))

    result_page.add_to_cart()

    WebDriverWait(browser, 30).until(EC.visibility_of_element_located(result_page.PAGEMESSAGE))

    assert "You added Erika Running Short to your shopping cart." in result_page.success_message()

    home_page.load()

    home_page.logout()
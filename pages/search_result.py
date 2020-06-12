"""
This module contains SearchResultPage,
"""

from selenium.webdriver.common.by import By


class SearchResultPage:
  
  # Locators

  SIZE = (By.ID, 'option-label-size-150-item-5599')
  COLOR = (By.ID, 'option-label-color-93-item-5480')
  ADDTOCARTBUTTON = (By.ID, 'product-addtocart-button')
  PAGEMESSAGE = (By.XPATH, '//*[@id="maincontent"]/div[1]/div[2]/div[2]/div/div')

  # Initializer

  def __init__(self, browser):
    self.browser = browser

  # Interaction Methods

  def add_to_cart(self):
    self.browser.find_element(*self.SIZE).click()
    self.browser.find_element(*self.COLOR).click()
    self.browser.find_element(*self.ADDTOCARTBUTTON).click()

  def success_message(self):
    message = self.browser.find_element(*self.PAGEMESSAGE)
    return message.text

"""
Class to model the basket/checkout of the SweetShop
"""

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pom.basepage import BasePage


class BasketPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = 'https://sweetshop.netlify.app/basket'
        self.page_heading = 'Your Basket'

    def select_free_collection(self):
        selector = '[for="exampleRadios1"]'
        self.driver.find_element(By.CSS_SELECTOR, selector).click()
        self.take_screenshot('select_free_collection')

    def select_standard_shipping(self):
        selector = '[for="exampleRadios2"]'
        self.driver.find_element(By.CSS_SELECTOR, selector).click()
        self.take_screenshot('select_standard_shipping')

    def basket_items(self):
        return self.driver.find_element(By.ID, 'basketItems').text

    def basket_total_is(self, expected_total):
        total_string = f'Total (GBP)\n{expected_total}'

        return total_string in self.basket_items()

"""
Class to model the homepage of the SweetShop
"""

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pom.basepage import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = 'https://sweetshop.netlify.app/'
        self.page_heading = 'Welcome to the sweet shop!'

    def add_first_sweet_to_basket(self):
        xpath = "/html/body/div/div[2]/div[2]/div/div[2]/a"
        self.driver.find_element(By.XPATH, xpath).click()
        self.take_screenshot('add_first_sweet_to_basket')

    def add_chocolate_cups_to_basket(self):
        selector = '[data-name="Chocolate Cups"]'
        self.driver.find_element(By.CSS_SELECTOR, selector).click()
        self.take_screenshot('add_first_sweet_to_basket')

    def add_strawberry_bon_bons_to_basket(self):
        selector = '[data-name="Strawberry Bon Bons"]'
        self.driver.find_element(By.CSS_SELECTOR, selector).click()
        self.take_screenshot('add_chocolate_cups_to_basket')

    def add_sherbet_discs_to_basket(self):
        selector = '[data-name="Sherbet Discs"]'
        self.driver.find_element(By.CSS_SELECTOR, selector).click()
        self.take_screenshot('add_sherbet_discs_to_basket')

    def add_sherbert_straws_to_basket(self):
        selector = '[data-name="Sherbert Straws"]'
        self.driver.find_element(By.CSS_SELECTOR, selector).click()
        self.take_screenshot('add_sherbert_straws_to_basket')

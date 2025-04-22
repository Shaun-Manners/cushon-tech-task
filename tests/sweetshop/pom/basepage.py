"""
Base page class that contains all common page methods
"""
import logging
import time
import datetime
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class BasePage:

    def __init__(self, driver):
        self.driver = driver

        self.page_url = ''
        self.page_title = 'Sweet Shop'
        self.page_heading = 'sweet'

        self.screenshot_dir = './screenshots/'

    def visit(self):
        self.driver.get(self.page_url)
        self.take_screenshot('homepage')

    def displayed(self):
        title_displayed = self.driver.title == self.page_title
        heading_displayed = self.page_heading in self.driver.page_source
        return title_displayed and heading_displayed

    def click_basket_link(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Basket').click()
        self.take_screenshot('clicked_basket')

    def take_screenshot(self, title):
        timestamp = time.time()
        datetime_timestamp = datetime.datetime.fromtimestamp(timestamp)
        formatted_timestamp = datetime_timestamp.strftime('%Y-%m-%d-%H-%M-%S')

        filename = f'{self.screenshot_dir}{formatted_timestamp}_{title}.png'
        logging.debug(f'Taken screenshot: {filename}')
        self.driver.save_screenshot(filename)

from support.browser import chrome_browser
from pom.basket import BasketPage
from pom.homepage import HomePage


def test_sweetshop_page_title():
    """
    Test the title of the sweetshop website
    """
    # Setup chrome and POM instances
    driver = chrome_browser()
    homepage = HomePage(driver)

    # Visit the sweetshop homepage
    homepage.visit()
    assert homepage.displayed()

    driver.quit()


def test_sweetshop_basket_total_standard_shipping():
    """
    Test the basket total after selecting:

    Chocolate cups: £1.00
    Sherbet discs: £0.95
    Standard Shipping: £1.99
    Total should be: £3.94
    """
    # Setup chrome and POM instances
    driver = chrome_browser()
    homepage = HomePage(driver)
    basket = BasketPage(driver)

    try:
        # Visit the sweetshop homepage
        homepage.visit()
        assert homepage.displayed()

        # Add two different sweets to the basket
        homepage.add_chocolate_cups_to_basket()
        homepage.add_sherbet_discs_to_basket()

        # Navigate to the basket
        homepage.click_basket_link()
        assert basket.displayed()

        # Select the standard shipping
        basket.select_standard_shipping()

        expected_total = '£3.94'
        total_string = f'Total (GBP)\n{expected_total}'
        assert total_string in basket.basket_items()

    finally:
        driver.quit()


def test_sweetshop_basket_total_collection():
    """
    Test the basket total after selecting:

    Chocolate cups: £1.00
    Sherbet discs: £0.95
    Collection: £0.00
    Total should be: £1.95
    """
    # Setup chrome and POM instances
    driver = chrome_browser()
    homepage = HomePage(driver)
    basket = BasketPage(driver)

    try:
        # Visit the sweetshop homepage
        homepage.visit()
        assert homepage.displayed()

        # Add two different sweets to the basket
        homepage.add_chocolate_cups_to_basket()
        homepage.add_sherbet_discs_to_basket()

        # Navigate to the basket
        homepage.click_basket_link()
        assert basket.displayed()

        # Select the standard shipping
        basket.select_free_collection()

        expected_total = '£1.95'
        total_string = f'Total (GBP)\n{expected_total}'
        assert total_string in basket.basket_items()

    finally:
        driver.quit()

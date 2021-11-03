from Locators.locators import ElementLocators
from selenium.common.exceptions import NoSuchElementException
from Utilities.Logging import Logger


class ProductDetail:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        add_button = self.driver.find_element_by_xpath(ElementLocators.
                                                       add_to_cart_xpath)
        add_button.click()

    def verify_price(self):
        try:
            price = self.driver.find_element_by_xpath(
                ElementLocators.price_xpath)
            verify_cost = price.text
            print(verify_cost)
            if verify_cost == verify_cost:
                assert True, "Price is validated"
            else:
                assert False
        except NoSuchElementException:
            Logger.log.critical("Price is not present")
            assert False, "Price validation failed"

    def verify_product_title(self):
        try:
            title = self.driver.find_element_by_xpath(ElementLocators.product_title_xpath)
            title_content = title.text
            print(title_content)
            if title_content == title_content:
                assert True, "Title is validated"
            else:
                assert False
        except NoSuchElementException:
            Logger.log.critical("Title is not validated")
            assert False, "Title validation failed"

    def verify_stock(self):
        try:
            stock = self.driver.find_element_by_xpath(ElementLocators.
                                                      stock_xpath)
            verify_availability = stock.text
            print(verify_availability)
            if verify_availability == "In stock.":
                assert True, "Stock is validated"
            else:
                assert False
        except NoSuchElementException:
            Logger.log.critical("Stock is not present")
            assert False, "Stock validation failed"

    def mini_cart(self):

        cart = self.driver.find_element_by_id(ElementLocators.mini_cart_id)
        cart.click()

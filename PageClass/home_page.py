from selenium.webdriver.support.ui import WebDriverWait
from Locators.locators import ElementLocators
from Utilities.Config_reader import read_config_data
from Base.base_class import BaseDriver


class HomePage(BaseDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def verify_home_page(self):
        if self.driver.current_url == read_config_data('details', 'URL'):
            assert True, "User is in Amazon"
        else:
            assert False, "User is not in Amazon"

    def navigate_to_home(self):
        logo = self.find_by_xpath(ElementLocators.logo_xpath)
        logo.click()

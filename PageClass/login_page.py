from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
# from Utilities.Logging import Logger
from selenium.webdriver.common.action_chains import ActionChains
from Locators.locators import ElementLocators
from Utilities.Config_reader import read_config_data


class Login:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.actions = ActionChains(self.driver)

    def click_login(self):
        login_button = self.driver.find_element_by_xpath(
            ElementLocators.login_xpath)
        login_button.click()

    def enter_email(self):
        email_field = self.driver.find_element_by_name(
            ElementLocators.email_field)
        email_field.send_keys(read_config_data('details', 'email'))

    def click_continue(self):
        continue_button = self.driver.find_element_by_class_name(
            ElementLocators.continue_button)
        continue_button.click()

    def enter_password(self):
        password_field = self.driver.find_element_by_name(
            ElementLocators.password_field)
        password_field.send_keys(read_config_data('details', 'password'))

    def verify_warning(self):
        try:
            self.driver.find_element_by_xpath(ElementLocators.warning_xpath)
            assert True, "Verified Invalid credentials"

        except NoSuchElementException:
            Logger.log.critical("Warning message not found")
            assert False, "Invalid Credentials verification failed"

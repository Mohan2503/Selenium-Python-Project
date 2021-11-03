from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from Locators.locators import ElementLocators


class ProductListing:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.actions = ActionChains(self.driver)

    def enter_search(self):
        search_field = self.driver.find_element_by_id(
            ElementLocators.search_id)
        search_field.send_keys(ElementLocators.search_term)

    def click_search(self):
        click_search = self.driver.find_element_by_id(
            ElementLocators.search_button_id)
        click_search.click()

    def choose_product(self):
        click_product = self.driver.find_element_by_partial_link_text(
            ElementLocators.product_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView()",
                                   click_product)
        click_product.click()
        windows = []
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])

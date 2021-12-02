class BaseDriver:

    def __init__(self, driver):
        self.driver = driver

    def find_by_xpath(self, locator):
        fxp = self.driver.find_element_by_xpath(locator)
        return fxp

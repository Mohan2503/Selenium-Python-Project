import pytest
from Utilities.Logging import Logger
from PageClass.list_page import ProductListing


@pytest.mark.usefixtures("setup")
class TestPlp:

    def test_product(self):
        try:
            Logger.log.info("Search and Select Product")
            list_1 = ProductListing(self.driver)
            list_1.enter_search()
            list_1.click_search()
            list_1.choose_product()
        except Exception as e:
            Logger.log.critical("Failed to Search and Select Product")
            assert False, str(e)

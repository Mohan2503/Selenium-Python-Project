import pytest
from Utilities.Logging import Logger
from PageClass.product_page import ProductDetail


@pytest.mark.usefixtures("setup")
class TestPdp:

    def test_add_product(self):
        try:
            Logger.log.info("Verifying Product details and adding to cart")
            pdp = ProductDetail(self.driver)
            pdp.verify_price()

            pdp.verify_stock()

            pdp.verify_product_title()

            pdp.add_to_cart()

            pdp.mini_cart()
        except Exception as e:
            Logger.log.critical("Failed to Verify Product details and add to cart")
            assert False, str(e)

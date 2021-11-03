import pytest
from Utilities.Logging import Logger
from PageClass.product_page import ProductDetail


@pytest.mark.usefixtures("setup")
class TestCart:

    def test_verify_cart(self):
        try:
            Logger.log.info("Verifying Cart page")
            cart = ProductDetail(self.driver)
            cart.verify_product_title()
            cart.verify_price()
        except Exception as e:
            Logger.log.critical("Invalid Product Title and Price in cart page")
            assert False, str(e)

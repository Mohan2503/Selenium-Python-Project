import pytest
from Utilities.Logging import Logger
from PageClass.home_page import HomePage


@pytest.mark.usefixtures("setup")
class TestHome:

    def test_verify_home_page(self):
        try:
            Logger.log.info("Verifying URL")
            home = HomePage(self.driver)
            home.verify_home_page()
            Logger.log.info("Valid URL")
        except Exception as e:
            Logger.log.critical("Invalid URL")
            assert False, str(e)

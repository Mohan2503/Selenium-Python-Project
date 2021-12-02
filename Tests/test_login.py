import pytest
from PageClass.login_page import Login
# from Utilities.Logging import Logger
from PageClass.home_page import HomePage


@pytest.mark.usefixtures("setup")
class TestLogin:

    def test_verify_login(self):
        try:
            # Logger.log.info("Verify Login")
            login = Login(self.driver)
            login.click_login()

            login.enter_email()

            login.click_continue()

            login.enter_password()
            login.click_continue()

            login.verify_warning()
        except Exception as e:
            # Logger.log.critical("Failed to Verify Login")
            assert False, str(e)

    def test_navigate_to_home(self):
        home = HomePage(self.driver)
        home.navigate_to_home()

import pytest
from selenium.webdriver import Chrome
from Utilities.Config_reader import read_config_data
from Locators.locators import ElementLocators


@pytest.fixture(scope="session")
def setup(request):
    driver = Chrome(executable_path=ElementLocators.chrome_driver)
    driver.maximize_window()
    driver.get(read_config_data('details', 'URL'))

    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", driver)

    yield
    driver.quit()

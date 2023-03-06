import pytest
from selenium import webdriver


class WebDriverWrapper:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        yield
        self.driver.quit()

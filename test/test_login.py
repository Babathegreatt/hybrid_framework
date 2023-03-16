import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

from base.webdriver_listner import WebDriverWrapper
from utilities import data_source


class TestLogin(WebDriverWrapper):

    def test_valid_login(self):

        login_page = LoginPage(self.driver)
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")

        # self.driver.find_element(By.NAME,"username").send_keys("Admin")
        # self.driver.find_element(By.NAME,"password").send_keys("admin123")
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        actual_text=self.driver.find_element(By.XPATH,"//h6[text()='Dashboard']").text
        assert_that("Dashboard").is_equal_to(actual_text)

    @pytest.mark.parametrize("username,password,expected_error",data_source.test_invalid_login_data)
    def test_invalid_login(self,username,password,expected_error):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        actual_error = self.driver.find_element(By.XPATH,"//p[normalize-space() = 'Invalid credentials']").text
        assert_that(expected_error).is_equal_to(actual_error)


class TestLoginUI(WebDriverWrapper):

    def test_title(self):

        actual_title=self.driver.title
        assert_that("OrangeHRM").is_equal_to(actual_title)

    def test_header(self):

        actual_header = self.driver.find_element(By.XPATH,"//h5[text()='Login']").text
        assert_that("Login").is_equal_to(actual_header)

    def test_login_placeholder(self):
        actual_username_placeholder= self.driver.find_element(By.NAME,"username").get_attribute("placeholder")
        actual_password_placeholder = self.driver.find_element(By.NAME, "password").get_attribute("placeholder")
        assert_that("Username").is_equal_to(actual_username_placeholder)
        assert_that("Password").is_equal_to(actual_password_placeholder)

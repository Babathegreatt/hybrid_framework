import time

import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By

from base.webdriver_listner import WebDriverWrapper
from utilities import data_source


class TestAddEmployee(WebDriverWrapper):

    @pytest.mark.parametrize("username,password,firstname,middlename,lastname,expected_profile_header,expected_firstname",data_source.test_add_valid_employee)
    def test_add_valid_employee(self,username,password,firstname,middlename,lastname,expected_profile_header,expected_firstname):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.XPATH,"//span[text()='PIM']").click()
        self.driver.find_element(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--secondary']").click()
        #Employee detaails
        self.driver.find_element(By.NAME,"firstName").send_keys(firstname)
        self.driver.find_element(By.NAME, "middleName").send_keys(middlename)
        self.driver.find_element(By.NAME, "lastName").send_keys(lastname)
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Save']").click()
        time.sleep(3)
        #Assert actual header and first name
        actual_header=self.driver.find_element(By.XPATH,f"//h6[contains(normalize-space(),'{firstname}')]").text
        first_name = self.driver.find_element(By.NAME, "firstName").get_attribute("value")

        assert_that(expected_profile_header).is_equal_to(actual_header)
        assert_that(expected_firstname).is_equal_to(first_name)

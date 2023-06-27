import pytest
import time
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class TestAddGenre():
    def setup_method(self, method):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(20)  # gives an implicit wait for 20 seconds
        self.vars = {}

    def test_addgenre(self):

        self.driver.get("https://hgfilm.ro-zum.eu/#grid-9_tab")
        self.driver.set_window_size(1124, 894)

        # login
        self.driver.find_element(By.NAME, "username").send_keys("mentalfvnda@gmail.com")  # login
        self.driver.find_element(By.NAME, "password").send_keys("retSoHn18")  # login
        self.driver.find_element(By.XPATH, "//div[@id='mylsAuthForm']/div/div/div/div[3]/div/div/div/div/span").click()
        time.sleep(2)

        # Click on Directories --> Genres
        self.driver.find_element(By.XPATH, "//div[normalize-space()='Directories']").click()
        wait = WebDriverWait(self.driver, 10)
        genres = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Genres')]")))
        genres.click()
        time.sleep(5)

        # add new Film type
        self.driver.find_element(
            By.XPATH, "//div[@id='grid-9_tab']/div/div[4]/div/div/div/div/div/div/div/img").click()
        time.sleep(2)
        self.driver.find_element(By.NAME, "genre_name_ru").send_keys("pyuic5456dsc")
        self.driver.find_element(By.XPATH, "//div[@id='form-10--1_popup_save-button']/div/span").click()
        time.sleep(2)

        # search for added element
        search_input = self.driver.find_element(By.XPATH, "//div[3]/div/div/div/div/div/input")
        search_input.click()
        search_input.send_keys("pyuic5456dsc")
        time.sleep(2)

        # Verify if the total records in the grid equals 1
        total_records = self.driver.find_element(By.XPATH, "//div[@id='grid-9_tab_totalCount']")
        total_records_value = total_records.text
        expected_count = '1'

        if expected_count in total_records_value:
            print("Total records is 1. Proceeding to deletion.")
            time.sleep(1)

            # delete record
            self.driver.find_element(By.XPATH,
                                     "//div[@id='grid-9_tab']/div/div[4]/div/div/div/div[3]/div/div/div/img").click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, "//span[contains(.,'Delete current')]").click()
            pass
            time.sleep(2)
            total_records_value = total_records.text
            expected_count_after_del = '0'

            if expected_count_after_del in total_records_value:
                print("Total records is 0.")

            else:
                # Assertion failed, handle the failure or raise an exception
                raise AssertionError(
                    f"Expected {expected_count_after_del} record, but found {total_records_value} records.")
        else:
            # Assertion failed, handle the failure or raise an exception
            raise AssertionError(f"Expected {expected_count} record, but found {total_records_value} records.")
        time.sleep(2)

        self.driver.close()
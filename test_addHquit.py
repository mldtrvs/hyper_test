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


class TestAddfilmtype():
    def setup_method(self, method):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(20)  # gives an implicit wait for 20 seconds
        self.vars = {}

    #def teardown_method(self, method):
    # self.driver.quit()

    def test_addfilmtype(self):

        self.driver.get("https://hgfilm.ro-zum.eu/#grid-331_tab")
        self.driver.set_window_size(1124, 894)

        # login
        self.driver.find_element(By.NAME, "username").send_keys("mentalfvnda@gmail.com")  # login
        self.driver.find_element(By.NAME, "password").send_keys("retSoHn18")  # login
        self.driver.find_element(By.XPATH, "//div[@id='mylsAuthForm']/div/div/div/div[3]/div/div/div/div/span").click()
        time.sleep(2)

        # close all tabs, open Film type menu
        self.driver.find_element(By.XPATH, "//div[@aria-label='dropdown']//img[@class='dx-icon']").click()
        time.sleep(1)
        self.driver.find_element(
            By.XPATH, "//b[contains(.,'Close all')]").click()
        # self.driver.find_element(By.XPATH, "//div[@id=\'toolbar\']/div/div/div/div/div/div/i").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[normalize-space()='Directories']").click()
        # Click on Genres
        wait = WebDriverWait(self.driver, 10)
        genres = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Genres')]")))
        genres.click()
        time.sleep(2)

        self.driver.close()
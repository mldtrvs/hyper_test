import pytest
import time
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from application import open_HGfilm, login_HGfilm

@pytest.fixture(scope="class")
def driver(request):
    driver = open_HGfilm()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield driver
    driver.quit()
class TestAddfilmtype():
    def setup_method(self):
        #options = webdriver.ChromeOptions()
        #options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome() #(options=options)
        self.driver.implicitly_wait(60)  # gives an implicit wait for 20 seconds
        #self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_addfilmtype(self):

        self.open_HGfilm()
        self.login_HGfilm(username="mentalfvnda@gmail.com", password="retSoHn18")
        #time.sleep(2)
        wait = self.go_to_film_types_menu()
        self.add_new_film_type(wait, film_type="eji4t3a4r3")
        time.sleep(2)
        self.search_for_new_film_type()

        # Verify if total records in the grid equals 1
        total_records = self.driver.find_element(By.XPATH,
                                                 "//div[@id='grid-331_tab']/div[2]/div/div/div/div/div")
        total_records_value = total_records.text
        expected_count = '1'

        if expected_count in total_records_value:
            print("Total records is 1. Proceeding to deletion.")
            time.sleep(1)

            # delete record
            self.driver.find_element(By.XPATH,
                                     "//div[@id=\'grid-331_tab\']/div/div[4]/div/div/div/div[3]/div/div/div").click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "/html/body/div[7]/div/div[3]/div/div[2]/div[1]/div/div/div").click()
            pass
            time.sleep(5)

            # Verify if total records in the grid equals 0
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

        #self.driver.close()

    def search_for_new_film_type(self):
        search_input = self.driver.find_element(By.XPATH, "//div[3]/div/div/div/div/div/input")
        search_input.click()
        search_input.send_keys("eji4t3a4r3")
        time.sleep(2)

    def add_new_film_type(self, wait, film_type):
        add_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@title='Add']//img[@class='dx-icon']")))
        add_btn.click()
        time.sleep(2)
        self.driver.find_element(By.NAME, "type_name").send_keys(film_type)
        ok_btn = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//div[@id='form-332--1_popup_save-button']//span[@class='dx-button-text'][normalize-space("
                      ")='Ok']")))
        ok_btn.click()

    def go_to_film_types_menu(self):
        # Open Directories --> Film types menu
        self.driver.find_element(By.XPATH, "//div[normalize-space()='Directories']").click()
        wait = WebDriverWait(self.driver, 10)
        film_types = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[normalize-space()='Film types']")))
        film_types.click()
        return wait

    def login_HGfilm(self, username, password):
        self.driver.find_element(By.NAME, "username").send_keys(username)  # login
        self.driver.find_element(By.NAME, "password").send_keys(password)  # login
        self.driver.find_element(By.XPATH, "//div[@id='mylsAuthForm']/div/div/div/div[3]/div/div/div/div/span").click()

    def open_HGfilm(self):
        self.driver.get("https://hgfilm.ro-zum.eu")
        self.driver.set_window_size(1124, 894)




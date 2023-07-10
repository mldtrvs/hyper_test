import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FilmTypeHelper:

    def __init__(self, app):
        self.app = app

    def go_to_film_types_menu(self):
        # Open Directories --> Film types menu
        self.app.driver.find_element(By.XPATH, "//div[normalize-space()='Directories']").click()
        wait = WebDriverWait(self.app.driver, 20)
        film_types = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[normalize-space()='Film types']")))
        film_types.click()
        return wait

    def add_new(self, wait, film_type):
        add_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#grid-331_tab [role=toolbar] ["
                                                                          "buttonrole=add]")))
        add_btn.click()
        time.sleep(3)
        self.app.driver.find_element(By.NAME, "type_name").send_keys(film_type)
        # ok_btn = wait.until(EC.element_to_be_clickable((
        #     By.XPATH, "//div[@id='form-332--1_popup_save-button']//span[@class='dx-button-text'][normalize-space("
        #               ")='Ok']")))
        ok_btn = wait.until(EC.element_to_be_clickable((By.ID, 'form-332--1_popup_save-button')))
        ok_btn.click()

    def search_for_new_added(self, film_type):
        search_input = self.app.driver.find_element(By.XPATH, "//*[@id='grid-331_tab']/div[1]/div[4]/div/div/div["
                                                              "3]/div[1]/div/div/div/div[1]/input")
        search_input.click()
        search_input.send_keys(film_type)
        time.sleep(2)

    def check_if_added_delete_check_if_deleted(self):
        # Verify if total records in the grid equals 1
        total_records = self.app.driver.find_element(By.XPATH,
                                                     "//div[@id='grid-331_tab']/div[2]/div/div/div/div/div")
        total_records_value = total_records.text
        expected_count = '1'
        if expected_count in total_records_value:
            print("Total records is 1. Proceeding to deletion.")
            time.sleep(1)

            # delete record
            self.app.driver.find_element(By.XPATH,
                                         "//div[@id=\'grid-331_tab\']/div/div[4]/div/div/div/div[3]/div/div/div").click()
            time.sleep(2)
            self.app.driver.find_element(By.XPATH, "/html/body/div[7]/div/div[3]/div/div[2]/div[1]/div/div/div").click()
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

import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GenresHelper:

    def __init__(self, app):
        self.app = app

    def go_to_genres(self):
        wait = WebDriverWait(self.app.driver, 10)
        genres = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".panel-list a[href='#grid-9_tab']")))
        genres.click()
        return wait

    def add_new(self, wait, genre):
        # add new Genre
        add_btn = wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "#grid-9_tab [role=toolbar] [buttonrole=add]")))
        add_btn.click()
        time.sleep(2)
        self.app.driver.find_element(By.NAME, "genre_name_ru").send_keys(genre)
        ok_btn = wait.until(
            EC.element_to_be_clickable((By.ID, "form-10--1_popup_save-button")))
        ok_btn.click()

    def search_for_new_added(self, genre):
        search_input = self.app.driver.find_element(By.CSS_SELECTOR, "#grid-9_tab [role=textbox]")
        search_input.click()
        search_input.clear()
        search_input.send_keys(genre)
        time.sleep(3)

    def check_total_records(self, expected_count):
        total_records = self.app.driver.find_element(By.ID, "grid-9_tab_totalCount")
        total_records_value = total_records.text

        if expected_count in total_records_value:
            print(f"Total records is {expected_count}.")
        else:
            # Assertion failed, handle the failure or raise an exception
            raise AssertionError(f"Expected {expected_count} record, but found {total_records_value} records.")

    def delete_record(self, wait):
        # delete record
        self.app.driver.find_element(By.CSS_SELECTOR,
                                     "#grid-9_tab [role=toolbar] [buttonrole=delete]").click()
        time.sleep(1)
        delete_current = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-button-type='grid"
                                                                                 "-9_tab_delete_current']")))
        delete_current.click()
        pass
        time.sleep(3)

    def check_if_added_delete_check_if_deleted(self, wait):
        # Verify if total records in the grid equals 1
        total_records = self.app.driver.find_element(By.ID, "grid-9_tab_totalCount")
        total_records_value = total_records.text
        expected_count = '1'

        if expected_count in total_records_value:
            print("Total records is 1. Proceeding to deletion.")
            time.sleep(1)
            self.delete_record(wait)
            time.sleep(3)
            self.check_total_records(expected_count='0')
        else:
            # Assertion failed, handle the failure or raise an exception
            raise AssertionError(f"Expected {expected_count} record, but found {total_records_value} records.")
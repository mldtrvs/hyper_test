import time

import pytest
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

    def add_new(self, wait, genre_ru, genre_en):
        # add new Genre
        add_btn = wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "#grid-9_tab [role=toolbar] [buttonrole=add]")))
        add_btn.click()
        self.app.driver.find_element(
            By.CSS_SELECTOR, "#form-10--1_popup [name='genre_name_ru']").send_keys(genre_ru)
        self.app.driver.find_element(
            By.CSS_SELECTOR, "#form-10--1_popup [name='genre_name_en']").send_keys(genre_en)

        ok_btn = wait.until(
            EC.element_to_be_clickable((By.ID, "form-10--1_popup_save-button")))
        ok_btn.click()

    def search_for_new_added(self, genre):
        search_input = self.app.driver.find_element(By.CSS_SELECTOR, "#grid-9_tab [role=textbox]")
        search_input.click()
        search_input.clear()
        search_input.send_keys(genre)
        time.sleep(3)

    def check_if_added(self):
        total_records = self.app.driver.find_element(By.ID, "grid-9_tab_totalCount")
        total_records_value = total_records.text
        expected_count = '1'
        try:
            if expected_count in total_records_value:
                print("Total records is 1. Proceeding to deletion.")
            else:
                # Assertion failed, handle the failure or raise an exception
                raise AssertionError(f"Expected {expected_count} record, but found {total_records_value} records.")
        except AssertionError as e:
            pytest.fail(f"Test failed: {e}")

    def delete_record(self, wait):
        delete_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                            "#grid-9_tab [role=toolbar] [buttonrole=delete]")))
        delete_btn.click()
        # self.app.driver.find_element(By.CSS_SELECTOR,
        #                              "#grid-9_tab [role=toolbar] [buttonrole=delete]").click()
        time.sleep(1)
        delete_current = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-button-type='grid"
                                                                                 "-9_tab_delete_current']")))
        delete_current.click()
        pass
        time.sleep(3)

    def check_if_deleted(self):
        total_records = self.app.driver.find_element(By.ID, "grid-9_tab_totalCount")
        total_records_value = total_records.text
        expected_count = '0'

        if expected_count in total_records_value:
            print("Total records is 0.")
        else:
            # Assertion failed, handle the failure or raise an exception
            raise AssertionError(f"Expected {expected_count} record, but found {total_records_value} records.")

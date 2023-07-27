import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DocumentTypeHelper:

    def __init__(self, app):
        self.app = app

    def go_to_document_types(self):
        wait = WebDriverWait(self.app.driver, 20)
        document_types = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".panel-list a[href='#grid-294_tab']")))
        document_types.click()
        return wait

    def add_new(self, wait, document_type_name):
        add_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#grid-294_tab [role=toolbar] ["
                                                                          "buttonrole=add]")))
        add_btn.click()
        self.app.driver.find_element(By.CSS_SELECTOR, "#form-295--1_popup [role=textbox]").send_keys(document_type_name)
        ok_btn = wait.until(EC.element_to_be_clickable((By.ID, 'form-295--1_popup_save-button')))
        ok_btn.click()

    def search_for_new_added(self, document_type_name):
        search_input = self.app.driver.find_element(By.CSS_SELECTOR, "#grid-294_tab [role=textbox]")
        search_input.click()
        search_input.clear()
        search_input.send_keys(document_type_name)
        time.sleep(3)

    def check_total_records(self, expected_count):
        total_records = self.app.driver.find_element(By.ID, "grid-294_tab_totalCount")
        total_records_value = total_records.text

        if expected_count in total_records_value:
            print(f"Total records is {expected_count}.")
        else:
            # Assertion failed, handle the failure or raise an exception
            raise AssertionError(f"Expected {expected_count} record, but found {total_records_value} records.")

    def check_if_added(self):
        total_records = self.app.driver.find_element(By.ID, "grid-294_tab_totalCount")
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

        self.app.driver.find_element(By.CSS_SELECTOR,
                                     "#grid-294_tab [role=toolbar] [buttonrole=delete]").click()
        time.sleep(1)
        delete_current = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-button-type='grid"
                                                                                 "-294_tab_delete_current']")))
        delete_current.click()
        pass
        time.sleep(3)

    def check_if_deleted(self):
        total_records = self.app.driver.find_element(By.ID, "grid-294_tab_totalCount")
        total_records_value = total_records.text
        expected_count = '0'

        if expected_count in total_records_value:
            print("Total records is 0.")
        else:
            # Assertion failed, handle the failure or raise an exception
            raise AssertionError(f"Expected {expected_count} record, but found {total_records_value} records.")
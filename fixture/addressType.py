import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class addressTypeHelper:

    def __init__(self, app):
        self.app = app

    def go_to_address_types(self):
        wait = WebDriverWait(self.app.driver, 20)
        document_types = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".panel-list a[href='#grid-310_tab']")))
        document_types.click()
        return wait

    def add_new(self, wait, address_type):
        add_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#grid-310_tab [role=toolbar] ["
                                                                          "buttonrole=add]")))
        add_btn.click()
        self.app.driver.find_element(By.CSS_SELECTOR, "#form-311--1_popup [name='type_name']").send_keys(address_type)
        ok_btn = wait.until(EC.element_to_be_clickable((By.ID, 'form-311--1_popup_save-button')))
        ok_btn.click()

    def search_for_new_added(self, address_type):
        search_input = self.app.driver.find_element(By.CSS_SELECTOR, "#grid-310_tab [role=textbox]")
        search_input.click()
        search_input.clear()
        search_input.send_keys(address_type)
        time.sleep(3)

    def check_if_added(self):
        total_records = self.app.driver.find_element(By.ID, "grid-310_tab_totalCount")
        total_records_value = total_records.text
        expected_count = '1'
        try:
            if expected_count in total_records_value:
                print("Total records is 1. Proceeding to next step.")
            else:
                # Assertion failed, handle the failure or raise an exception
                raise AssertionError(f"Expected {expected_count} record, but found {total_records_value} records.")
        except AssertionError as e:
            pytest.fail(f"Test failed: {e}")

    def edit(self, wait, address_type):
        record_id_number = self.get_record_id()

        edit_btn = wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "#grid-310_tab [role=toolbar] [buttonrole=edit]")))
        edit_btn.click()
        address_type_edit = self.app.driver.find_element(
            By.CSS_SELECTOR, f"#form-311-{record_id_number}_popup [name='type_name']")
        address_type_edit.clear()
        address_type_edit.send_keys(address_type)

        ok_btn = wait.until(
            EC.element_to_be_clickable((By.ID, f"form-311-{record_id_number}_popup_save-button")))
        ok_btn.click()

    def get_record_id(self):
        record_id = self.app.driver.find_element(By.ID, "grid-310_tab_totalId")
        text = record_id.text
        record_id_number = text.split(":")[1].strip()
        # print(record_id_number)
        return record_id_number

    def delete_record(self, wait):

        self.app.driver.find_element(By.CSS_SELECTOR,
                                     "#grid-310_tab [role=toolbar] [buttonrole=delete]").click()
        time.sleep(1)
        delete_current = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-button-type='grid"
                                                                                 "-310_tab_delete_current']")))
        delete_current.click()
        pass
        time.sleep(3)

    def check_if_deleted(self):
        total_records = self.app.driver.find_element(By.ID, "grid-310_tab_totalCount")
        total_records_value = total_records.text
        expected_count = '0'

        if expected_count in total_records_value:
            print("Total records is 0.")
        else:
            # Assertion failed, handle the failure or raise an exception
            raise AssertionError(f"Expected {expected_count} record, but found {total_records_value} records.")

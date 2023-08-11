import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ageRestrictionHelper:

    def __init__(self, app):
        self.app = app

    def go_to_age_restrictions(self):
        wait = WebDriverWait(self.app.driver, 20)
        age_restrictions = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".panel-list a[href='#grid-333_tab']")))
        age_restrictions.click()
        return wait

    def add_new(self, wait, age_restriction):
        add_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#grid-333_tab [role=toolbar] ["
                                                                          "buttonrole=add]")))
        add_btn.click()
        self.app.driver.find_element(By.CSS_SELECTOR, "#form-334--1_popup [name='age_limit']").send_keys(age_restriction)
        ok_btn = wait.until(EC.element_to_be_clickable((By.ID, 'form-334--1_popup_save-button')))
        ok_btn.click()

    def search_for_new_added(self, age_restriction):
        search_input = self.app.driver.find_element(By.CSS_SELECTOR, "#grid-333_tab [role=textbox]")
        search_input.click()
        search_input.clear()
        search_input.send_keys(age_restriction)
        time.sleep(3)

    def check_if_added(self):
        total_records = self.app.driver.find_element(By.ID, "grid-333_tab_totalCount")
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

    def edit(self, wait, edit):
        record_id_number = self.get_record_id()

        edit_btn = wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "#grid-333_tab [role=toolbar] [buttonrole=edit]")))
        edit_btn.click()
        age_restriction_edit = self.app.driver.find_element(
            By.CSS_SELECTOR, f"#form-334-{record_id_number}_popup [name='age_limit']")
        age_restriction_edit.clear()
        age_restriction_edit.send_keys(edit)

        ok_btn = wait.until(
            EC.element_to_be_clickable((By.ID, f"form-334-{record_id_number}_popup_save-button")))
        ok_btn.click()

    def get_record_id(self):
        record_id = self.app.driver.find_element(By.ID, "grid-333_tab_totalId")
        text = record_id.text
        record_id_number = text.split(":")[1].strip()
        # print(record_id_number)
        return record_id_number

    def delete_record(self, wait):

        self.app.driver.find_element(By.CSS_SELECTOR,
                                     "#grid-333_tab [role=toolbar] [buttonrole=delete]").click()
        time.sleep(1)
        delete_current = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-button-type='grid"
                                                                                 "-333_tab_delete_current']")))
        delete_current.click()
        pass
        time.sleep(3)

    def check_if_deleted(self):
        total_records = self.app.driver.find_element(By.ID, "grid-333_tab_totalCount")
        total_records_value = total_records.text
        expected_count = '0'

        if expected_count in total_records_value:
            print("Total records is 0.")
        else:
            # Assertion failed, handle the failure or raise an exception
            raise AssertionError(f"Expected {expected_count} record, but found {total_records_value} records.")

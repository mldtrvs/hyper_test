import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class docDetailsHelper:

    def __init__(self, app):
        self.app = app

    def go_to_doc_details(self):
        wait = WebDriverWait(self.app.driver, 10)
        tags = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".panel-list a[href='#grid-308_tab']")))
        tags.click()
        return wait

    def open_new_form(self, detail_name, wait):
        add_btn = wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "#grid-308_tab [role=toolbar] [buttonrole=add]")))
        add_btn.click()
        self.app.driver.find_element(By.CSS_SELECTOR, "#form-309--1_popup [name=type_name]").send_keys(detail_name)
        affiliation_selector = self.app.driver.find_element(By.CSS_SELECTOR, "#form-309--1_popup "
                                                                             ".data-myls__is_legal .dx-selectbox")
        affiliation_selector.click()
        aria_owns_value = affiliation_selector.get_attribute("aria-owns")
        print(aria_owns_value)
        return aria_owns_value

    def choose_affiliation(self, aria_owns_value, div_index):
        affiliation = self.app.driver.find_element(
            By.CSS_SELECTOR, f"#{aria_owns_value} [role=listbox]>div:nth-child({div_index})")
        affiliation_text_in = affiliation.text
        print(affiliation_text_in)
        affiliation.click()
        return affiliation_text_in

    def save_form(self, wait):
        ok_btn = wait.until(
            EC.visibility_of_element_located((By.ID, "form-309--1_popup_save-button")))
        ok_btn.click()

    def search_for_new_added(self, detail_name):
        search_input = self.app.driver.find_element(By.CSS_SELECTOR, "#grid-308_tab [role=textbox]")
        search_input.click()
        search_input.clear()
        search_input.send_keys(detail_name)

    def get_affiliation_value(self):
        record_id = self.app.driver.find_element(By.ID, "grid-308_tab_totalId")
        text = record_id.text
        record_id_number = text.split(":")[1].strip()
        print(record_id_number)

        wait = WebDriverWait(self.app.driver, 10)
        affiliation_value = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, f"#grid-308_tab [data-id='{record_id_number}']")))
        affiliation_text_out = affiliation_value.text
        print(affiliation_text_out)
        return affiliation_text_out

    def check_selected_affiliation_match(self, affiliation_text_in, affiliation_text_out):
        if affiliation_text_in in affiliation_text_out:
            print("Affiliation match")
        else:
            raise AssertionError(f"Affiliation values differs. Expected: {affiliation_text_in}, Actual: {affiliation_text_out}")

    def check_if_added(self):
        total_records = self.app.driver.find_element(By.ID, "grid-308_tab_totalCount")
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
                                     "#grid-308_tab [role=toolbar] [buttonrole=delete]").click()
        time.sleep(1)
        delete_current = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-button-type='grid"
                                                                                 "-308_tab_delete_current']")))
        delete_current.click()
        pass
        time.sleep(4)

    def check_if_deleted(self):
        total_records = self.app.driver.find_element(By.ID, "grid-308_tab_totalCount")
        total_records_value = total_records.text
        expected_count = '0'

        if expected_count in total_records_value:
            print("Total records is 0.")
        else:
            # Assertion failed, handle the failure or raise an exception
            raise AssertionError(f"Expected {expected_count} record, but found {total_records_value} records.")

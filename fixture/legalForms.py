import time

import pytest
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class legalFormHelper:

    def __init__(self, app):
        self.app = app

    def go_to_legal_forms(self):
        wait = WebDriverWait(self.app.driver, 2)
        try:
            legal_forms = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".panel-list a[href='#grid-342_tab']")))
        except TimeoutException:
            self.scroll_menu(wait)
            legal_forms = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".panel-list a[href='#grid-342_tab']")))
        legal_forms.click()

    def scroll_menu(self, wait):
        menu_scrollbar = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.panel-list .dx-scrollable-scroll')))
        action_chains = ActionChains(self.app.driver)
        action_chains.move_to_element(menu_scrollbar).perform()
        action_chains.drag_and_drop_by_offset(menu_scrollbar, 0, 164).perform()

    def add_new(self, legal_form_name):
        wait = WebDriverWait(self.app.driver, 10)
        add_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#grid-342_tab [role=toolbar] ["
                                                                          "buttonrole=add]")))
        add_btn.click()
        self.app.driver.find_element(By.CSS_SELECTOR, "#form-344--1_popup [role=textbox]").send_keys(legal_form_name)
        ok_btn = wait.until(EC.element_to_be_clickable((By.ID, 'form-344--1_popup_save-button')))
        ok_btn.click()
        return wait

    def add_new_SP_attribute_checkbox(self, legal_form_name):
        wait = WebDriverWait(self.app.driver, 10)
        add_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#grid-342_tab [role=toolbar] ["
                                                                          "buttonrole=add]")))
        add_btn.click()
        self.app.driver.find_element(By.CSS_SELECTOR, '#form-344--1_popup [role=checkbox]').click()
        self.app.driver.find_element(By.CSS_SELECTOR, "#form-344--1_popup [role=textbox]").send_keys(legal_form_name)
        ok_btn = wait.until(EC.element_to_be_clickable((By.ID, 'form-344--1_popup_save-button')))
        ok_btn.click()
        return wait

    def search_for_new_added(self, legal_form_name):
        search_input = self.app.driver.find_element(By.CSS_SELECTOR, "#grid-342_tab [role=textbox]")
        search_input.click()
        search_input.clear()
        search_input.send_keys(legal_form_name)
        time.sleep(3)

    def if_checkbox_true(self):
        record_id_number = self.get_record_id()
        wait = WebDriverWait(self.app.driver, 10)
        element = wait.until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR,
                f"#grid-342_tab [data-id='{record_id_number}'] td:not(.dx-command-select) .dx-checkbox")))
        checkbox_value = element.get_attribute("aria-checked")
        print("checkbox:", checkbox_value)
        if checkbox_value == "false":
            pytest.fail("Checkbox value is False.")

    def get_record_id(self):
        record_id = self.app.driver.find_element(By.ID, "grid-342_tab_totalId")
        text = record_id.text
        record_id_number = text.split(":")[1].strip()
        return record_id_number

    def check_if_added(self):
        total_records = self.app.driver.find_element(By.ID, "grid-342_tab_totalCount")
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
                                     "#grid-342_tab [role=toolbar] [buttonrole=delete]").click()
        time.sleep(1)
        delete_current = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-button-type='grid"
                                                                                 "-342_tab_delete_current']")))
        delete_current.click()
        pass
        time.sleep(3)

    def check_if_deleted(self):
        total_records = self.app.driver.find_element(By.ID, "grid-342_tab_totalCount")
        total_records_value = total_records.text
        expected_count = '0'

        if expected_count in total_records_value:
            print("Total records is 0.")
        else:
            # Assertion failed, handle the failure or raise an exception
            raise AssertionError(f"Expected {expected_count} record, but found {total_records_value} records.")

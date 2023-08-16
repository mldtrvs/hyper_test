import time

import pytest
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class releaseTypeHelper:
    def __init__(self, app):
        self.app = app

    def go_to_release_type(self):
        wait = WebDriverWait(self.app.driver, 2)
        try:
            positions = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".panel-list a[href='#grid-407_tab']")))
        except TimeoutException:
            self.scroll_menu(wait)
            positions = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".panel-list a[href='#grid-407_tab']")))
        positions.click()

    def scroll_menu(self, wait):
        menu_scrollbar = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.panel-list .dx-scrollable-scroll')))
        action_chains = ActionChains(self.app.driver)
        action_chains.move_to_element(menu_scrollbar).perform()
        action_chains.drag_and_drop_by_offset(menu_scrollbar, 0, 164).perform()

    def add_new(self, release_type):
        wait = WebDriverWait(self.app.driver, 10)
        add_btn = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#grid-407_tab [role=toolbar] [buttonrole=add]')))
        add_btn.click()
        self.app.driver.find_element(By.CSS_SELECTOR, "#form-458--1_popup [name='type_name']").send_keys(release_type)
        ok_btn = wait.until(EC.element_to_be_clickable((By.ID, 'form-458--1_popup_save-button')))
        ok_btn.click()
        return wait

    def search_for_new_added(self, release_type):
        search_input = self.app.driver.find_element(By.CSS_SELECTOR, "#grid-407_tab [role=textbox]")
        search_input.click()
        search_input.clear()
        search_input.send_keys(release_type)
        time.sleep(3)

    def check_if_added(self):
        total_records = self.app.driver.find_element(By.ID, "grid-407_tab_totalCount")
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

    def edit(self, wait, edit):
        record_id_number = self.get_record_id()

        edit_btn = wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "#grid-407_tab [role=toolbar] [buttonrole=edit]")))
        edit_btn.click()
        release_name_edit = self.app.driver.find_element(
            By.CSS_SELECTOR, f"#form-458-{record_id_number}_popup [name='type_name']")
        release_name_edit.clear()
        release_name_edit.send_keys(edit)

        ok_btn = wait.until(
            EC.element_to_be_clickable((By.ID, f"form-458-{record_id_number}_popup_save-button")))
        ok_btn.click()

    def get_record_id(self):
        record_id = self.app.driver.find_element(By.ID, "grid-407_tab_totalId")
        text = record_id.text
        record_id_number = text.split(":")[1].strip()
        # print(record_id_number)
        return record_id_number

    def delete_record(self, wait):

        self.app.driver.find_element(By.CSS_SELECTOR,
                                     "#grid-407_tab [role=toolbar] [buttonrole=delete]").click()
        time.sleep(1)
        delete_current = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-button-type='grid"
                                                                                 "-407_tab_delete_current']")))
        delete_current.click()
        pass
        time.sleep(3)

    def check_if_deleted(self):
        total_records = self.app.driver.find_element(By.ID, "grid-407_tab_totalCount")
        total_records_value = total_records.text
        expected_count = '0'

        if expected_count in total_records_value:
            print("Total records is 0.")
        else:
            # Assertion failed, handle the failure or raise an exception
            raise AssertionError(f"Expected {expected_count} record, but found {total_records_value} records.")

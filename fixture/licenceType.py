import time

import pytest
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class licenceTypeHelper:
    def __init__(self, app):
        self.app = app

    def go_to_licence_type(self):
        wait = WebDriverWait(self.app.driver, 2)
        try:
            positions = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".panel-list a[href='#grid-314_tab']")))
        except TimeoutException:
            self.scroll_menu(wait)
            positions = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".panel-list a[href='#grid-314_tab']")))
        positions.click()
        return wait

    def scroll_menu(self, wait):
        menu_scrollbar = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.panel-list .dx-scrollable-scroll')))
        action_chains = ActionChains(self.app.driver)
        action_chains.move_to_element(menu_scrollbar).perform()
        action_chains.drag_and_drop_by_offset(menu_scrollbar, 0, 164).perform()

    def open_new_form(self, licence_name, wait, descrp):
        add_btn = wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "#grid-314_tab [role=toolbar] [buttonrole=add]")))
        add_btn.click()
        self.app.driver.find_element(By.CSS_SELECTOR, "#form-315--1_popup [name='type_name']").send_keys(licence_name)
        self.app.driver.find_element(By.CSS_SELECTOR, "#form-315--1_popup [name='description']").send_keys(descrp)
        type_selector = self.app.driver.find_element(By.CSS_SELECTOR, "#form-315--1_popup [role=combobox]")
        type_selector.click()
        aria_owns_value = type_selector.get_attribute("aria-owns")
        print(aria_owns_value)
        return aria_owns_value


    def choose_licence_type(self, aria_owns_value, div_index):
        licence_type = self.app.driver.find_element(
            By.CSS_SELECTOR, f"#{aria_owns_value} [role=listbox]>div:nth-child({div_index})")
        licence_type_text_in = licence_type.text
        print(licence_type_text_in)
        licence_type.click()
        return licence_type_text_in

    def save_form(self, wait):
        ok_btn = wait.until(
            EC.visibility_of_element_located((By.ID, "form-315--1_popup_save-button")))
        ok_btn.click()

    def search_for_new_added(self, licence_name):
        search_input = self.app.driver.find_element(By.CSS_SELECTOR, "#grid-314_tab [role=textbox]")
        search_input.click()
        search_input.clear()
        search_input.send_keys(licence_name)

    def get_licence_type_value(self):
        record_id = self.app.driver.find_element(By.ID, "grid-314_tab_totalId")
        text = record_id.text
        record_id_number = text.split(":")[1].strip()
        print(record_id_number)

        wait = WebDriverWait(self.app.driver, 10)
        licence_type_value = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, f"#grid-314_tab [data-id='{record_id_number}']")))
        licence_type_text_out = licence_type_value.text
        print(licence_type_text_out)
        return licence_type_text_out

    def check_selected_licence_type_match(self, licence_type_text_in, licence_type_text_out):
        if licence_type_text_in in licence_type_text_out:
            print("Licence type match")
        else:
            raise AssertionError(f"Licence type values differ. Expected: {licence_type_text_in}, Actual: {licence_type_text_out}")

    def check_if_added(self):
        total_records = self.app.driver.find_element(By.ID, "grid-314_tab_totalCount")
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
            By.CSS_SELECTOR, "#grid-314_tab [role=toolbar] [buttonrole=edit]")))
        edit_btn.click()
        licence_name_edit = self.app.driver.find_element(
            By.CSS_SELECTOR, f"#form-315-{record_id_number}_popup [name='type_name']")
        licence_name_edit.clear()
        licence_name_edit.send_keys(edit)

        ok_btn = wait.until(
            EC.element_to_be_clickable((By.ID, f"form-315-{record_id_number}_popup_save-button")))
        ok_btn.click()

    def get_record_id(self):
        record_id = self.app.driver.find_element(By.ID, "grid-314_tab_totalId")
        text = record_id.text
        record_id_number = text.split(":")[1].strip()
        # print(record_id_number)
        return record_id_number

    def delete_record(self, wait):

        self.app.driver.find_element(By.CSS_SELECTOR,
                                     "#grid-314_tab [role=toolbar] [buttonrole=delete]").click()
        time.sleep(1)
        delete_current = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-button-type='grid"
                                                                                 "-314_tab_delete_current']")))
        delete_current.click()
        pass
        time.sleep(4)

    def check_if_deleted(self):
        total_records = self.app.driver.find_element(By.ID, "grid-314_tab_totalCount")
        total_records_value = total_records.text
        expected_count = '0'

        if expected_count in total_records_value:
            print("Total records is 0.")
        else:
            # Assertion failed, handle the failure or raise an exception
            raise AssertionError(f"Expected {expected_count} record, but found {total_records_value} records.")

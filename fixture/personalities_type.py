import time

import pytest
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class personalitiesTypeHelper:

    def __init__(self, app):
        self.app = app

    def go_to_person_type(self):
        wait = WebDriverWait(self.app.driver, 2)
        try:
            positions = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".panel-list a[href='#grid-381_tab']")))
        except TimeoutException:
            self.scroll_menu(wait)
            positions = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".panel-list a[href='#grid-381_tab']")))
        positions.click()
        return wait

    def scroll_menu(self, wait):
        menu_scrollbar = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.panel-list .dx-scrollable-scroll')))
        action_chains = ActionChains(self.app.driver)
        action_chains.move_to_element(menu_scrollbar).perform()
        action_chains.drag_and_drop_by_offset(menu_scrollbar, 0, 164).perform()

    def add_new(self, wait, person_type_ru , person_type_en):
        # add new Genre
        add_btn = wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "#grid-381_tab [role=toolbar] [buttonrole=add]")))
        add_btn.click()
        self.app.driver.find_element(By.CSS_SELECTOR,
                                     "#form-382--1_popup .dx-box-flex > :nth-child(1) [role=textbox]").send_keys(person_type_ru)
        self.app.driver.find_element(By.CSS_SELECTOR,
                                     "#form-382--1_popup .dx-box-flex > :nth-child(2) [role=textbox]").send_keys(person_type_en)
        ok_btn = wait.until(
            EC.element_to_be_clickable((By.ID, "form-382--1_popup_save-button")))
        ok_btn.click()

    def search_for_new_added_ru(self, person_type):
        search_input = self.app.driver.find_element(By.CSS_SELECTOR, "#grid-381_tab [role=textbox]")
        search_input.click()
        search_input.clear()
        search_input.send_keys(person_type)
        time.sleep(3)

    def search_for_new_added_en(self, person_type_en):
        search_input = self.app.driver.find_element(By.CSS_SELECTOR, "#grid-381_tab [role=textbox]")
        search_input.click()
        search_input.clear()
        search_input.send_keys(person_type_en)
        time.sleep(3)

    def check_if_added(self):
        total_records = self.app.driver.find_element(By.ID, "grid-381_tab_totalCount")
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
                                                            "#grid-381_tab [role=toolbar] [buttonrole=delete]")))
        delete_btn.click()
        # self.app.driver.find_element(By.CSS_SELECTOR,
        #                              "#grid-9_tab [role=toolbar] [buttonrole=delete]").click()
        time.sleep(1)
        delete_current = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-button-type='grid"
                                                                                 "-381_tab_delete_current']")))
        delete_current.click()
        pass
        time.sleep(3)

    def check_if_deleted(self):
        total_records = self.app.driver.find_element(By.ID, "grid-381_tab_totalCount")
        total_records_value = total_records.text
        expected_count = '0'

        if expected_count in total_records_value:
            print("Total records is 0.")
        else:
            # Assertion failed, handle the failure or raise an exception
            raise AssertionError(f"Expected {expected_count} record, but found {total_records_value} records.")
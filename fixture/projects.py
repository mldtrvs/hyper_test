import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class projectHelper:

    def __init__(self, app):
        self.app = app

    def go_to_projects(self):
        wait = WebDriverWait(self.app.driver, 10)
        projects = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".panel-list a[href='#grid-276_tab']")))
        projects.click()
        return wait

    def open_new_form(self, wait, title):
        add_btn = wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "#grid-276_tab [role=toolbar] [buttonrole=add]")))
        add_btn.click()

        self.app.driver.find_element(
            By.CSS_SELECTOR, "#form-277--1_popup [name='title_ru']").send_keys(title)

        production_type_selector = self.app.driver.find_element(By.CSS_SELECTOR, "#form-277--1_popup "
                                                                                 ".data-myls__project_type_id "
                                                                                 ".dx-selectbox")
        production_type_selector.click()
        aria_owns_value = production_type_selector.get_attribute("aria-owns")
        print(aria_owns_value)
        return aria_owns_value

    def choose_production_type(self, aria_owns_value, div_index):
        production_type = self.app.driver.find_element(
            By.CSS_SELECTOR, f"#{aria_owns_value} [role=listbox]>div:nth-child({div_index})")
        production_type_text_in = production_type.text
        print(production_type_text_in)
        production_type.click()
        return production_type_text_in

    def choose_genre_type(self, div_index_gt):
        genre_type_selector = self.app.driver.find_element(By.CSS_SELECTOR,
                                                  "#form-277--1_popup .data-myls__genres [role=combobox]")
        genre_type_selector.click()
        gt_aria_owns_value = genre_type_selector.get_attribute("aria-owns")
        print(gt_aria_owns_value)
        genre_type = self.app.driver.find_element(
            By.CSS_SELECTOR, f"#{gt_aria_owns_value} [role=listbox]>div:nth-child({div_index_gt})")
        genre_type_text_in = genre_type.text
        print(genre_type_text_in)
        genre_type.click()
        genre_type_selector.click()
        return gt_aria_owns_value, genre_type

    def save_form(self, wait):
        ok_btn = wait.until(
            EC.visibility_of_element_located((By.ID, "form-277--1_popup_save-button")))
        ok_btn.click()

    def search_for_new_added(self, wait, title):
        wait.until(EC.invisibility_of_element((By.CSS_SELECTOR, "form-277--1_popup")))
        search_input = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#grid-276_tab [role=textbox]")))
        search_input.click()
        search_input.clear()
        search_input.send_keys(title)

    def check_if_added(self):
        total_records = self.app.driver.find_element(By.ID, "grid-276_tab_totalCount")
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

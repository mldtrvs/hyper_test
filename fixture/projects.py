import time

import pytest
import random

from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
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

    def production_type_own_production(self, aria_owns_value, wait):
        production_type = self.app.driver.find_element(
            By.CSS_SELECTOR, f"#{aria_owns_value} [role=listbox]>div:nth-child(3)")
        production_type.click()

        start_date = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#form-277--1_popup [name='start_date_right']")))

        start_date.click()
        start_date.send_keys("10.10.2023")

        try:
            # Check if the readonly element exists
            self.app.driver.find_element(By.CSS_SELECTOR, "#form-277--1_popup .dx-state-readonly")
        except NoSuchElementException:
            # If it doesn't exist, send keys to the start_date element
            start_date = self.app.driver.find_element(By.CSS_SELECTOR, "#form-277--1_popup [name='start_date_right']")

            start_date.click()
            start_date.send_keys("10.10.2023")
        else:
            # Handle the case where the readonly element exists (optional)
            # You can log a message or perform other actions if needed.
            print("Start date is in readonly state.")

        #return production_type_text_in

    def random_choice_production_type(self, aria_owns_value, wait):
        production_type_elements = self.app.driver.find_elements(
            By.CSS_SELECTOR, f"#{aria_owns_value} [role=listbox]>div")
        random_index = random.randint(1, len(production_type_elements))
        selected_production_type = production_type_elements[random_index - 1]
        production_type_text_in = selected_production_type.text
        print(production_type_text_in)

        selected_production_type.click()

        try:
            # Check if the readonly element exists
            self.app.driver.find_element(By.CSS_SELECTOR, "#form-277--1_popup .dx-state-readonly")
        except NoSuchElementException:
            # If it doesn't exist, send keys to the start_date element
            start_date = self.app.driver.find_element(By.CSS_SELECTOR, "#form-277--1_popup [name='start_date_right']")

            start_date.click()
            start_date.send_keys("10.10.2023")
        else:
            # Handle the case where the readonly element exists (optional)
            # You can log a message or perform other actions if needed.
            print("Start date is in readonly state.")

        return production_type_text_in

    def random_choice_genre_type(self):
        genre_type_selector = self.app.driver.find_element(By.CSS_SELECTOR,
                                                           "#form-277--1_popup .data-myls__genres [role=combobox]")
        genre_type_selector.click()
        gt_aria_owns_value = genre_type_selector.get_attribute("aria-owns")
        print(gt_aria_owns_value)

        # Get the total number of checkboxes available
        checkboxes = self.app.driver.find_elements(By.CSS_SELECTOR, f"#{gt_aria_owns_value} [role=checkbox]>div")
        total_checkboxes = len(checkboxes)
        print(total_checkboxes)

        # Generate a list of random indices, excluding div_index_gt
        random_indices = [i for i in range(2, total_checkboxes + 1)]  # if i != div_index_gt]

        # Randomly choose the number of checkboxes to select between 1 and the total number of checkboxes
        num_checkboxes_to_select = random.randint(1, total_checkboxes)

        # Randomly select a subset of checkboxes
        selected_indices = random.sample(random_indices, num_checkboxes_to_select)

        for index in selected_indices:
            genre_type = self.app.driver.find_element(
                By.CSS_SELECTOR, f"#{gt_aria_owns_value} [role=listbox]>div:nth-child({index})")
            genre_type_text_in = genre_type.text
            print(f"Selected genre type: {genre_type_text_in}")
            genre_type.click()

        genre_type_selector.click()
        return gt_aria_owns_value, selected_indices

    def scroll_menu(self, wait, gt_aria_owns_value):
        menu_scrollbar = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, f"#{gt_aria_owns_value} .dx-scrollable-scroll")))
        action_chains = ActionChains(self.app.driver)
        action_chains.move_to_element(menu_scrollbar).perform()
        action_chains.drag_and_drop_by_offset(menu_scrollbar, 0, 164).perform()

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

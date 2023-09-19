import time

import pytest
import random

from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class projectHelper:

    def __init__(self, app):
        self.app = app

    def go_to_projects(self):
        wait = WebDriverWait(self.app.driver, 20)
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

        try:
            # Check if the readonly element exists
            self.app.driver.find_element(By.CSS_SELECTOR, "#form-277--1_popup .dx-state-readonly")
        except NoSuchElementException:
            # If it doesn't exist, send keys to the start_date element
            start_date = self.app.driver.find_element(By.CSS_SELECTOR,
                                                      "#form-277--1_popup [name=start_date_right] + div input")

            start_date.click()
            start_date.send_keys("10.10.2023")
            self.app.driver.find_element(By.CSS_SELECTOR, "#form-277--1_popup-tab_0_image_file-image").click()
        else:
            # Handle the case where the readonly element exists (optional)
            print("Start date is in readonly state.")

    def random_choice_production_type(self, aria_owns_value):
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
            start_date = self.app.driver.find_element(By.CSS_SELECTOR,
                                                      "#form-277--1_popup [name=start_date_right] + div input")

            start_date.click()
            start_date.send_keys("10.10.2023")
            self.app.driver.find_element(By.CSS_SELECTOR, "#form-277--1_popup-tab_0_image_file-image").click()
        else:
            # Handle the case where the readonly element exists (optional)
            print("Start date is in readonly state.")

        return production_type_text_in

    def random_choice_genre_type(self, wait):
        genre_type_selector = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#form-277--1_popup"
                                                                                      "-tab_0_genres_tagbox")))
        genre_type_selector.click()
        gt_aria_owns_value = genre_type_selector.get_attribute("aria-owns")
        print(gt_aria_owns_value)

        checkboxes = wait.until(
            EC.presence_of_all_elements_located((
                By.CSS_SELECTOR, f"#{gt_aria_owns_value} [role=option]")))

        checkboxes_text = []
        for checkbox in checkboxes:
            # Using JavaScript to retrieve the text of the checkbox, even if it's not visible
            checkbox_text = self.app.driver.execute_script("return arguments[0].textContent;", checkbox)
            checkboxes_text.append(checkbox_text)

        # Generate a random number of checkboxes to select
        min_checkboxes_to_select = 1  # Minimum number of checkboxes to select
        # max_checkboxes_to_select = len(checkboxes_text)  # Maximum number of checkboxes to select
        # num_checkboxes_to_select = random.randint(min_checkboxes_to_select, max_checkboxes_to_select)
        num_checkboxes_to_select = random.randint(1, 6)

        # Randomly select checkboxes
        random_checkboxes = random.sample(checkboxes_text, num_checkboxes_to_select)

        # Print the randomly selected checkboxes
        print("Randomly selected checkboxes:")
        for selected_checkbox in random_checkboxes:
            print(selected_checkbox)

        # Input the randomly selected text into the genre_type_selector element with "Enter" key presses
        genre_type_input = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#form-277--1_popup-tab_0_genres_tagbox [role=combobox]")))
        genre_type_input.click()

        for i, selected_checkbox in enumerate(random_checkboxes):
            genre_type_input.send_keys(selected_checkbox)

            # Press "Enter" after each checkbox, except for the last one
            if i < len(random_checkboxes) - 1:
                genre_type_input.send_keys(Keys.ENTER)

        time.sleep(1)
        self.app.driver.find_element(By.CSS_SELECTOR, "#form-277--1_popup-tab_0_image_file-image").click()

        return gt_aria_owns_value, random_checkboxes

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

    def get_record_id(self):
        record_id = self.app.driver.find_element(By.ID, "grid-276_tab_totalId")
        text = record_id.text
        record_id_number = text.split(":")[1].strip()
        # print(record_id_number)
        return record_id_number

    def scroll_horizontally_until_visible(self, element):
        current_scroll_left = 0
        max_scroll_left = self.app.driver.execute_script(
            "return document.documentElement.scrollWidth - window.innerWidth;")

        while current_scroll_left < max_scroll_left:
            try:
                # Try to find the element
                element.is_displayed()
                break  # Element is visible, exit the loop
            except:
                # Element is not visible, scroll right
                current_scroll_left += 100  # Adjust the scroll amount as needed
                self.app.driver.execute_script(f"window.scrollTo({current_scroll_left}, 0);")
                time.sleep(1)  # Add a sleep to allow the page to load and update

    def get_production_type_value(self):
        record_id_number = self.get_record_id()
        print(record_id_number)

        wait = WebDriverWait(self.app.driver, 10)
        production_type_selector = (By.CSS_SELECTOR, f"#grid-276_tab [data-id='{record_id_number}']")
        production_type_value = wait.until(
            EC.presence_of_element_located(production_type_selector))

        self.scroll_horizontally_until_visible(production_type_value)

        # production_type_value = wait.until(
        #     EC.visibility_of_element_located((By.CSS_SELECTOR, f"#grid-276_tab [data-id='{record_id_number}']")))

        production_type_text_out = production_type_value.text
        print(production_type_text_out)
        return production_type_text_out

    def check_selected_production_type_match(self, production_type_text_in, production_type_text_out):
        if production_type_text_in in production_type_text_out:
            print("Tag type match")
        else:
            raise AssertionError(
                f"Tag type values differ. Expected: {production_type_text_in}, Actual: {production_type_text_out}")

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

    def delete_record(self, wait):

        self.app.driver.find_element(By.CSS_SELECTOR,
                                     "#grid-276_tab [role=toolbar] [buttonrole=delete]").click()
        time.sleep(1)
        delete_current = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-button-type='grid"
                                                                                 "-276_tab_delete_current']")))
        delete_current.click()
        pass
        time.sleep(4)

    def check_if_deleted(self):
        total_records = self.app.driver.find_element(By.ID, "grid-276_tab_totalCount")
        total_records_value = total_records.text
        expected_count = '0'

        if expected_count in total_records_value:
            print("Total records is 0.")
        else:
            # Assertion failed, handle the failure or raise an exception
            raise AssertionError(f"Expected {expected_count} record, but found {total_records_value} records.")

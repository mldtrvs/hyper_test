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

        # # Get the total number of checkboxes available
        # checkboxes = wait.until(
        #     EC.visibility_of_all_elements_located((By.CSS_SELECTOR, f"#{gt_aria_owns_value} [role=checkbox]>div")))
        # total_checkboxes = len(checkboxes)
        # print(total_checkboxes)
        # return gt_aria_owns_value, total_checkboxes

        checkboxes = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, f"#{gt_aria_owns_value} [role=option]")))
        total_checkboxes = len(checkboxes)
        print(total_checkboxes)

        # Create a list of only the visible checkboxes
        visible_checkboxes = [checkbox for checkbox in checkboxes if checkbox.is_displayed()]
        len_visible_checkboxes = len(visible_checkboxes)
        print(len_visible_checkboxes)

        # Check if there are any visible checkboxes
        if len(visible_checkboxes) > 0:
            # Set the maximum number of checkboxes to select equal to the number of visible checkboxes
            max_num_to_select = len(visible_checkboxes)

            # Ensure that at least one checkbox is selected, and the maximum is the number of visible checkboxes
            num_to_select = random.randint(1, max_num_to_select)

            # Randomly select checkboxes from the list of visible checkboxes
            selected_checkboxes = random.sample(visible_checkboxes, num_to_select)

            # Click on the selected checkboxes
            for checkbox in selected_checkboxes:
                checkbox.click()
        else:
            print("No visible checkboxes found on the page.")

        while len(visible_checkboxes) > 0:
            # Scroll down to the last visible checkbox
            last_visible_checkbox = visible_checkboxes[-1]
            self.app.driver.execute_script("arguments[0].scrollIntoView();", last_visible_checkbox)

            # Wait for a short time to allow the page to load and update visibility
            time.sleep(1)

            # Update the list of visible checkboxes
            visible_checkboxes = [checkbox for checkbox in checkboxes if checkbox.is_displayed()]

            if len(visible_checkboxes) > 0:
                # Set the maximum number of checkboxes to select equal to the number of visible checkboxes
                max_num_to_select = len(visible_checkboxes)

                # Ensure that at least one checkbox is selected, and the maximum is the number of visible checkboxes
                num_to_select = random.randint(1, max_num_to_select)

                # Randomly select checkboxes from the list of visible checkboxes
                selected_checkboxes = random.sample(visible_checkboxes, num_to_select)

                # Click on the selected checkboxes
                for checkbox in selected_checkboxes:
                    checkbox.click()

                last_visible_checkbox = visible_checkboxes[-1]
                self.app.driver.execute_script("arguments[0].scrollIntoView();", last_visible_checkbox)

                # Wait for a short time to allow the page to load and update visibility
                time.sleep(1)

                # Update the list of visible checkboxes
                visible_checkboxes = [checkbox for checkbox in checkboxes if checkbox.is_displayed()]

                if len(visible_checkboxes) > 0:
                    # Set the maximum number of checkboxes to select equal to the number of visible checkboxes
                    max_num_to_select = len(visible_checkboxes)

                    # Ensure that at least one checkbox is selected, and the maximum is the number of visible checkboxes
                    num_to_select = random.randint(1, max_num_to_select)

                    # Randomly select checkboxes from the list of visible checkboxes
                    selected_checkboxes = random.sample(visible_checkboxes, num_to_select)

                    # Click on the selected checkboxes
                    for checkbox in selected_checkboxes:
                        checkbox.click()
                    last_visible_checkbox = visible_checkboxes[-1]
                    self.app.driver.execute_script("arguments[0].scrollIntoView();", last_visible_checkbox)

                    # Wait for a short time to allow the page to load and update visibility
                    time.sleep(1)

                    # Update the list of visible checkboxes
                    visible_checkboxes = [checkbox for checkbox in checkboxes if checkbox.is_displayed()]
                    if len(visible_checkboxes) > 0:
                        # Set the maximum number of checkboxes to select equal to the number of visible checkboxes
                        max_num_to_select = len(visible_checkboxes)

                        # Ensure that at least one checkbox is selected, and the maximum is the number of visible checkboxes
                        num_to_select = random.randint(1, max_num_to_select)

                        # Randomly select checkboxes from the list of visible checkboxes
                        selected_checkboxes = random.sample(visible_checkboxes, num_to_select)

                        # Click on the selected checkboxes
                        for checkbox in selected_checkboxes:
                            checkbox.click()
                        last_visible_checkbox = visible_checkboxes[-1]
                        self.app.driver.execute_script("arguments[0].scrollIntoView();", last_visible_checkbox)

                        # Wait for a short time to allow the page to load and update visibility
                        time.sleep(1)

                        # Update the list of visible checkboxes
                        visible_checkboxes = [checkbox for checkbox in checkboxes if checkbox.is_displayed()]
                        if len(visible_checkboxes) > 0:
                            # Set the maximum number of checkboxes to select equal to the number of visible checkboxes
                            max_num_to_select = len(visible_checkboxes)

                            # Ensure that at least one checkbox is selected, and the maximum is the number of visible checkboxes
                            num_to_select = random.randint(1, max_num_to_select)

                            # Randomly select checkboxes from the list of visible checkboxes
                            selected_checkboxes = random.sample(visible_checkboxes, num_to_select)

                            # Click on the selected checkboxes
                            for checkbox in selected_checkboxes:
                                checkbox.click()
                            last_visible_checkbox = visible_checkboxes[-1]
                            self.app.driver.execute_script("arguments[0].scrollIntoView();", last_visible_checkbox)

                            # Wait for a short time to allow the page to load and update visibility
                            time.sleep(1)

                            # Update the list of visible checkboxes
                            visible_checkboxes = [checkbox for checkbox in checkboxes if checkbox.is_displayed()]

        # All visible checkboxes have become invisible
        print("All visible checkboxes have become invisible.")

        self.app.driver.find_element(By.CSS_SELECTOR, "#form-277--1_popup-tab_0_image_file-image").click()

        return gt_aria_owns_value, total_checkboxes

    def scroll_genres(self, gt_aria_owns_value, wait):
        menu_scrollbar = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, f"#{gt_aria_owns_value} .dx-scrollable-scroll")))
        action_chains = ActionChains(self.app.driver)
        action_chains.move_to_element(menu_scrollbar).perform()
        action_chains.drag_and_drop_by_offset(menu_scrollbar, 0, 116).perform()

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

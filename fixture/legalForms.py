import time

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
            positions = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".panel-list a[href='#grid-342_tab']")))
        except TimeoutException:
            self.scroll_menu(wait)
            positions = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".panel-list a[href='#grid-342_tab']")))
        positions.click()
        return positions

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
        time.sleep(2)
        self.app.driver.find_element(By.NAME, "form_name").send_keys(legal_form_name)
        ok_btn = wait.until(EC.element_to_be_clickable((By.ID, 'form-344--1_popup_save-button')))
        ok_btn.click()

    def add_new_SP_attribute_checkbox(self, legal_form_name):
        wait = WebDriverWait(self.app.driver, 10)
        add_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#grid-342_tab [role=toolbar] ["
                                                                          "buttonrole=add]")))
        add_btn.click()
        time.sleep(2)
        self.app.driver.find_element(By.CSS_SELECTOR, '#form-344--1_popup [role=checkbox]').click()
        self.app.driver.find_element(By.NAME, "form_name").send_keys(legal_form_name)
        ok_btn = wait.until(EC.element_to_be_clickable((By.ID, 'form-344--1_popup_save-button')))
        ok_btn.click()

    def search_for_new_added(self, legal_form_name):
        search_input = self.app.driver.find_element(By.CSS_SELECTOR, "#grid-342_tab [role=textbox]")
        search_input.click()
        search_input.clear()
        search_input.send_keys(legal_form_name)
        time.sleep(3)

    def check_total_records(self, expected_count):
        total_records = self.app.driver.find_element(By.ID, "grid-342_tab_totalCount")
        total_records_value = total_records.text

        if expected_count in total_records_value:
            print(f"Total records is {expected_count}.")
        else:
            # Assertion failed, handle the failure or raise an exception
            raise AssertionError(f"Expected {expected_count} record, but found {total_records_value} records.")

    def delete_record(self):
        # delete record
        self.app.driver.find_element(By.CSS_SELECTOR,
                                     "#grid-342_tab [role=toolbar] [buttonrole=delete]").click()
        time.sleep(1)
        wait = WebDriverWait(self.app.driver, 10)
        delete_current = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-button-type='grid"
                                                                                 "-342_tab_delete_current']")))
        delete_current.click()
        pass
        time.sleep(3)

    def check_if_added_delete_check_if_deleted(self):
        # Verify if total records in the grid equals 1
        total_records = self.app.driver.find_element(By.ID, "grid-342_tab_totalCount")
        total_records_value = total_records.text
        expected_count = '1'

        if expected_count in total_records_value:
            print("Total records is 1. Proceeding to deletion.")
            time.sleep(1)
            self.delete_record()
            time.sleep(3)
            self.check_total_records(expected_count='0')
        else:
            # Assertion failed, handle the failure or raise an exception
            raise AssertionError(f"Expected {expected_count} record, but found {total_records_value} records.")
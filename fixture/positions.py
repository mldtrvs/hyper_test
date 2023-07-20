import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class positionsHelper:

    def __init__(self, app):
        self.app = app

    def go_to_positions(self):
        wait = WebDriverWait(self.app.driver, 5)
        positions = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".panel-list a[href='#grid-383_tab']")))
        if not positions.is_displayed():
            # 1
            menu_scrollbar = self.app.driver.find_element(By.CSS_SELECTOR, 'panel-list .dx-scrollable-scroll')
            menu_scrollbar.click()
            self.app.driver.execute_script("arguments[0].scroll(0,arguments[0].scrollHeight);", menu_scrollbar)
            # menu_scrollbar = self.app.driver.find_element(By.CSS_SELECTOR, '.panel-list .dx-scrollable-scroll')
            # menu_scrollbar.click()
            # actions = ActionChains(self.app.driver)
            # actions.move_to_element(menu_scrollbar).perform()
            # menu_scrollbar = self.app.driver.find_element(By.CSS_SELECTOR, '.panel-list .dx-scrollable-scrollbar')
            # self.app.driver.execute_script("arguments[0].scrollBy(0, 100);", menu_scrollbar)
            time.sleep(1)

        positions.click()
        return wait

    def add_new(self, wait, position_name):
        add_btn = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#grid-383_tab [role=toolbar] [buttonrole=add]')))
        add_btn.click()
        time.sleep(2)
        self.app.driver.find_element(By.NAME, "post_name").send_keys(position_name)
        ok_btn = wait.until(EC.element_to_be_clickable((By.ID, 'form-457--1_popup_save-button')))
        ok_btn.click()

    def search_for_new_added(self, position_name):
        search_input = self.app.driver.find_element(By.CSS_SELECTOR, "#grid-383_tab [role=textbox]")
        search_input.click()
        search_input.send_keys(position_name)
        time.sleep(1)

    def check_total_records(self, expected_count):
        total_records = self.app.driver.find_element(By.ID, "grid-383_tab_totalCount")
        total_records_value = total_records.text

        if expected_count in total_records_value:
            print(f"Total records is {expected_count}.")
        else:
            # Assertion failed, handle the failure or raise an exception
            raise AssertionError(f"Expected {expected_count} record, but found {total_records_value} records.")

    def delete_record(self, wait):
        # delete record
        self.app.driver.find_element(By.CSS_SELECTOR,
                                     "#grid-383_tab [role=toolbar] [buttonrole=delete]").click()
        time.sleep(1)
        delete_current = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-button-type='grid"
                                                                                 "-383_tab_delete_current']")))
        delete_current.click()
        pass
        time.sleep(2)

    def check_if_added_delete_check_if_deleted(self, wait):
        # Verify if total records in the grid equals 1
        total_records = self.app.driver.find_element(By.ID, "grid-383_tab_totalCount")
        total_records_value = total_records.text
        expected_count = '1'

        if expected_count in total_records_value:
            print("Total records is 1. Proceeding to deletion.")
            time.sleep(1)
            self.delete_record(wait)
            self.check_total_records(expected_count='0')
        else:
            # Assertion failed, handle the failure or raise an exception
            raise AssertionError(f"Expected {expected_count} record, but found {total_records_value} records.")

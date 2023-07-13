import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class addressTypeHelper:

    def __init__(self, app):
        self.app = app

    def go_to_address_types(self):
        # Open Directories --> address types menu
        directories_dropdown = self.app.driver.find_element(By.CSS_SELECTOR,
                                                            ".panel-list [role=listbox]>div:nth-child("
                                                            "6)>.dx-list-group-body")
        if not directories_dropdown.is_displayed():
            directories = self.app.driver.find_element(
                By.CSS_SELECTOR, ".panel-list [role=listbox]>div:nth-child(6)>div:first-child")
            directories.click()
        wait = WebDriverWait(self.app.driver, 20)
        document_types = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".panel-list a[href='#grid-310_tab']")))
        document_types.click()
        return wait

    def add_new(self, wait, address_type):
        add_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#grid-310_tab [role=toolbar] ["
                                                                          "buttonrole=add]")))
        add_btn.click()
        time.sleep(2)
        self.app.driver.find_element(By.NAME, "type_name").send_keys(address_type)
        ok_btn = wait.until(EC.element_to_be_clickable((By.ID, 'form-311--1_popup_save-button')))
        ok_btn.click()

    def search_for_new_added(self, address_type):
        search_input = self.app.driver.find_element(By.CSS_SELECTOR, "#grid-310_tab [role=textbox]")
        search_input.click()
        search_input.send_keys(address_type)
        time.sleep(1)

    def check_if_added_delete_check_if_deleted(self, wait):
        # Verify if total records in the grid equals 1
        total_records = self.app.driver.find_element(By.ID,
                                                     "grid-310_tab_totalCount")
        total_records_value = total_records.text
        expected_count = '1'
        if expected_count in total_records_value:
            print("Total records is 1. Proceeding to deletion.")
            time.sleep(1)

            # delete record
            self.app.driver.find_element(By.CSS_SELECTOR,
                                         "#grid-310_tab [role=toolbar] [buttonrole=delete]").click()
            time.sleep(1)
            delete_current = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-button-type='grid"
                                                                                     "-310_tab_delete_current']")))
            delete_current.click()
            pass
            time.sleep(1)

            # Verify if total records in the grid equals 0
            total_records_value = total_records.text
            expected_count_after_del = '0'

            if expected_count_after_del in total_records_value:
                print("Total records is 0.")

            else:
                # Assertion failed, handle the failure or raise an exception
                raise AssertionError(
                    f"Expected {expected_count_after_del} record, but found {total_records_value} records.")

        else:
            # Assertion failed, handle the failure or raise an exception
            raise AssertionError(f"Expected {expected_count} record, but found {total_records_value} records.")
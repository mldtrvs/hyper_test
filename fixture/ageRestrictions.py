import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ageRestrictionHelper:

    def __init__(self, app):
        self.app = app

    def go_to_age_restrictions(self):
        # Open Directories --> address types menu
        # directories_dropdown = self.app.driver.find_element(By.CSS_SELECTOR,
        #                                                     ".panel-list [role=listbox]>div:nth-child("
        #                                                     "6)>.dx-list-group-body")
        # if not directories_dropdown.is_displayed():
        #     directories = self.app.driver.find_element(
        #         By.CSS_SELECTOR, ".panel-list [role=listbox]>div:nth-child(6)>div:first-child")
        #     directories.click()
        wait = WebDriverWait(self.app.driver, 20)
        age_restrictions = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".panel-list a[href='#grid-333_tab']")))
        age_restrictions.click()
        return wait

    def add_new(self, wait, age_restriction):
        add_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#grid-333_tab [role=toolbar] ["
                                                                          "buttonrole=add]")))
        add_btn.click()
        time.sleep(2)
        self.app.driver.find_element(By.NAME, "age_limit").send_keys(age_restriction)
        ok_btn = wait.until(EC.element_to_be_clickable((By.ID, 'form-334--1_popup_save-button')))
        ok_btn.click()

    def search_for_new_added(self, age_restriction):
        search_input = self.app.driver.find_element(By.CSS_SELECTOR, "#grid-333_tab [role=textbox]")
        search_input.click()
        search_input.send_keys(age_restriction)
        time.sleep(1)

    def check_if_added_delete_check_if_deleted(self, wait):
        # Verify if total records in the grid equals 1
        total_records = self.app.driver.find_element(By.ID,
                                                     "grid-333_tab_totalCount")
        total_records_value = total_records.text
        expected_count = '1'
        if expected_count in total_records_value:
            print("Total records is 1. Proceeding to deletion.")
            time.sleep(1)

            # delete record
            self.app.driver.find_element(By.CSS_SELECTOR,
                                         "#grid-333_tab [role=toolbar] [buttonrole=delete]").click()
            time.sleep(1)
            delete_current = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-button-type='grid"
                                                                                     "-333_tab_delete_current']")))
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
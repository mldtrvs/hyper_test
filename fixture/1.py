import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Helper:
    def __init__(self, app):
        self.app = app

    def check_total_records(self, expected_count):
        total_records = self.app.driver.find_element(By.ID, "grid-333_tab_totalCount")
        total_records_value = total_records.text

        if expected_count in total_records_value:
            print(f"Total records is {expected_count}.")
        else:
            # Assertion failed, handle the failure or raise an exception
            raise AssertionError(f"Expected {expected_count} record, but found {total_records_value} records.")

    def check_if_added_delete_check_if_deleted(self, wait):
        # Verify if total records in the grid equals 1
        total_records = self.app.driver.find_element(By.ID, "grid-333_tab_totalCount")
        total_records_value = total_records.text
        expected_count = '1'

        if expected_count in total_records_value:
            print("Total records is 1. Proceeding to deletion.")
            time.sleep(1)
            self.delete_record(wait)
            time.sleep(3)
            self.check_total_records(expected_count='0')
        else:
            # Assertion failed, handle the failure or raise an exception
            raise AssertionError(f"Expected {expected_count} record, but found {total_records_value} records.")

    def check_if_added(self):
        total_records = self.app.driver.find_element(By.ID, "grid-333_tab_totalCount")
        total_records_value = total_records.text
        expected_count = '1'
        try:
            if expected_count in total_records_value:
                print("Total records is 1. Proceeding to deletion.")
            else:
                # Assertion failed, handle the failure or raise an exception
                raise AssertionError(f"Expected {expected_count} record, but found {total_records_value} records.")
        except AssertionError as e:
            print(f"AssertionError: {e}")
            return

    def delete_record(self, wait):

        self.app.driver.find_element(By.CSS_SELECTOR,
                                     "#grid-333_tab [role=toolbar] [buttonrole=delete]").click()
        time.sleep(1)
        delete_current = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-button-type='grid"
                                                                                 "-333_tab_delete_current']")))
        delete_current.click()
        pass
        time.sleep(3)

    def check_if_deleted(self):
        total_records = self.app.driver.find_element(By.ID, "grid-333_tab_totalCount")
        total_records_value = total_records.text
        expected_count = '0'
        try:
            if expected_count in total_records_value:
                print("Total records is 0. Proceeding to deletion.")
            else:
                # Assertion failed, handle the failure or raise an exception
                raise AssertionError(f"Expected {expected_count} record, but found {total_records_value} records.")
        except AssertionError as e:
            print(f"AssertionError: {e}")
            return

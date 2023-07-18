import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class statusesHelper:

    def __init__(self, app):
        self.app = app

    def go_to_statuses(self):
        wait = WebDriverWait(self.app.driver, 10)
        statuses = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".panel-list a[href='#grid-15_tab']")))
        statuses.click()
        return wait

    def add_new(self, wait, status_name):
        # add new Status
        add_btn = wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "#grid-15_tab [role=toolbar] [buttonrole=add]")))
        add_btn.click()
        time.sleep(2)
        self.app.driver.find_element(By.NAME, "status_name").send_keys(status_name)
        type_selector = self.app.driver.find_element(By.CSS_SELECTOR, "#form-16--1_popup "
                                                                      ".data-myls__sys_status_type_id .dx-selectbox")
        type_selector.click()
        aria_owns_value = type_selector.get_attribute("aria-owns")
        print(aria_owns_value)
        status_type = self.app.driver.find_elements(By.CSS_SELECTOR, "#" + aria_owns_value + " [role=listbox] [role=option]")
        print(len(status_type))
        # на кино! #form-16--1_popup .data-myls__sys_status_type_id .dx-selectbox кликнуть
        # после клика найти aria-owns опотом в этом  # dx-e426bd8b-f2c1-cdf5-d69a-3d39bd676f52 и там уже искать элементы списка

        # time.sleep(1)
        # ok_btn = wait.until(
        #     EC.element_to_be_clickable((By.ID, "form-16--1_popup_save-button")))
        # ok_btn.click()

    def search_for_new_added(self, genre):
        search_input = self.app.driver.find_element(By.CSS_SELECTOR, "#grid-15_tab [role=textbox]")
        search_input.send_keys(genre)
        time.sleep(1)

    def check_if_added_delete_check_if_deleted(self, wait):
        total_records = self.app.driver.find_element(By.ID, "grid-15_tab_totalCount")
        total_records_value = total_records.text
        expected_count = '1'
        if expected_count in total_records_value:
            print("Total records is 1. Proceeding to deletion.")
            time.sleep(1)

            # delete record
            self.app.driver.find_element(By.CSS_SELECTOR,
                                         "#grid-15_tab [role=toolbar] [buttonrole=delete]").click()
            time.sleep(1)
            delete_current = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-button-type='grid"
                                                                                     "-15_tab_delete_current']")))
            delete_current.click()
            pass
            time.sleep(1)
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

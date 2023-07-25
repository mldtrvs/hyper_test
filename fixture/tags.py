import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class tagsHelper:

    def __init__(self, app):
        self.app = app

    def go_to_tags(self):
        wait = WebDriverWait(self.app.driver, 10)
        tags = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".panel-list a[href='#grid-63_tab']")))
        tags.click()
        return wait

    def open_new_form(self, tag_name, wait):
        add_btn = wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "#grid-63_tab [role=toolbar] [buttonrole=add]")))
        add_btn.click()
        time.sleep(2)
        self.app.driver.find_element(By.NAME, "tag").send_keys(tag_name)
        type_selector = self.app.driver.find_element(By.CSS_SELECTOR, "#form-62--1_popup .data-myls__sys_tag_type_id "
                                                                      ".dx-selectbox")
        type_selector.click()
        aria_owns_value = type_selector.get_attribute("aria-owns")
        print(aria_owns_value)
        return aria_owns_value

    def choose_tag_type(self, aria_owns_value, div_index):
        tag_type = self.app.driver.find_element(
            By.CSS_SELECTOR, f"#{aria_owns_value} [role=listbox]>div:nth-child({div_index})")
        tag_type.click()

    def save_form(self, wait):
        time.sleep(4)
        ok_btn = wait.until(
            EC.visibility_of_element_located((By.ID, "form-62--1_popup_save-button")))
        ok_btn.click()
    
    def search_for_new_added(self, tag_name):
        search_input = self.app.driver.find_element(By.CSS_SELECTOR, "#grid-63_tab [role=textbox]")
        search_input.click()
        search_input.clear()
        search_input.send_keys(tag_name)
        time.sleep(3)

        idn = self.app.driver.find_element(By.ID, "grid-63_tab_totalId")
        text = idn.text
        extracted_number = text.split(":")[1].strip()
        print(extracted_number)
        time.sleep(3)
        wait = WebDriverWait(self.app.driver, 10)
        typevalue = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, f"#grid-63_tab [data-id='{extracted_number}']>td:nth-child(3)")))
        text = typevalue.text
        print(text)

    def check_total_records(self, expected_count):
        total_records = self.app.driver.find_element(By.ID, "grid-63_tab_totalCount")
        total_records_value = total_records.text

        if expected_count in total_records_value:
            print(f"Total records is {expected_count}.")
        else:
            # Assertion failed, handle the failure or raise an exception
            raise AssertionError(f"Expected {expected_count} record, but found {total_records_value} records.")

    def delete_record(self, wait):
        # delete record
        self.app.driver.find_element(By.CSS_SELECTOR,
                                     "#grid-63_tab [role=toolbar] [buttonrole=delete]").click()
        time.sleep(1)
        delete_current = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-button-type='grid"
                                                                                 "-63_tab_delete_current']")))
        delete_current.click()
        pass
        time.sleep(3)

    def check_if_added_delete_check_if_deleted(self, wait):
        # Verify if total records in the grid equals 1
        total_records = self.app.driver.find_element(By.ID, "grid-63_tab_totalCount")
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



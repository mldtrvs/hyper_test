import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GenresHelper:

    def __init__(self, app):
        self.app = app

    def go_to_genres(self):
        # Click on Directories --> Genres
        # self.app.driver.find_element(
        #     By.CSS_SELECTOR, ".panel-list [role=listbox]>div:nth-child(6)>div:first-child").click()
        wait = WebDriverWait(self.app.driver, 10)
        genres = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".panel-list a[href='#grid-9_tab']")))
        genres.click()
        return wait

    def add_new(self, wait, genre):
        # add new Genre
        add_btn = wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "#grid-9_tab [role=toolbar] [buttonrole=add]")))
        add_btn.click()
        time.sleep(2)
        self.app.driver.find_element(By.NAME, "genre_name_ru").send_keys(genre)
        # ok_btn = wait.until(
        #     EC.element_to_be_clickable((By.XPATH, "//div[@id='form-10--1_popup_save-button']/div/span")))
        ok_btn = wait.until(
            EC.element_to_be_clickable((By.ID, "form-10--1_popup_save-button")))
        ok_btn.click()

    def search_for_new_added(self, genre):
        # search for added element
        #search_input = self.app.driver.find_element(By.XPATH, "//div[3]/div/div/div/div/div/input")
        search_input = self.app.driver.find_element(By.CSS_SELECTOR, "#grid-9_tab [role=textbox]")
        search_input.send_keys(genre)
        time.sleep(2)

    def check_if_added_delete_check_if_deleted(self, wait):
        total_records = self.app.driver.find_element(By.ID, "grid-9_tab_totalCount")
        total_records_value = total_records.text
        expected_count = '1'
        if expected_count in total_records_value:
            print("Total records is 1. Proceeding to deletion.")
            time.sleep(1)

            # delete record
            self.app.driver.find_element(By.XPATH,
                                         "//div[@id='grid-9_tab']/div/div[4]/div/div/div/div[3]/div/div/div/img").click()
            time.sleep(1)
            delete_current = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div/div[3]/div/div["
                                                                              "2]/div[1]/div/div/div/span")))
            delete_current.click()
            #self.app.driver.find_element(By.XPATH, "//span[contains(.,'Delete current')]").click()
            pass
            time.sleep(2)
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

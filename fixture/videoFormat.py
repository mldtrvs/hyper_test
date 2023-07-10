import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class VideoFormatHelper:

    def __init__(self, app):
        self.app = app

    def go_to_video_format(self):
        # Click on Directories --> Genres
        #self.app.driver.find_element(By.XPATH, "//div[normalize-space()='Directories']").click()
        wait = WebDriverWait(self.app.driver, 10)
        video_format = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='drawer']/div/div[1]/div/div[2]/div/div[1]/div[2]/div[6]/div[2]/div[3]/div/a")))
        video_format.click()
        return wait

    def add_new(self, wait, video_format):
        # add new video format
        add_btn = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//*[@id='grid-292_tab']/div[1]/div[4]/div/div/div[1]/div[1]/div/div/div/img")))
        add_btn.click()
        time.sleep(2)
        self.app.driver.find_element(By.NAME, "format_name").send_keys(video_format)
        ok_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='form-293--1_popup_save-button']/div/span")))
        ok_btn.click()

    def search_for_new_added(self, video_format):
        # search for added element
        search_input = self.app.driver.find_element(By.XPATH, "//div[3]/div/div/div/div/div/input")
        search_input.click()
        search_input.send_keys(video_format)
        time.sleep(2)

    def check_if_added_delete_check_if_deleted(self, wait):
        total_records = self.app.driver.find_element(By.XPATH, "//*[@id='grid-292_tab_totalCount']")
        total_records_value = total_records.text
        expected_count = '1'
        if expected_count in total_records_value:
            print("Total records is 1. Proceeding to deletion.")
            time.sleep(1)

            # delete record
            self.app.driver.find_element(
                By.XPATH, "//*[@id='grid-292_tab']/div[1]/div[4]/div/div/div[1]/div[3]/div/div/div/img").click()
            time.sleep(1)
            delete_current = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[8]/div/div[3]/div/div["
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
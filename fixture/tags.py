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
        type_selector = self.app.driver.find_element(By.CSS_SELECTOR, "#form-62--1_popup "
                                                                      ".data-myls__sys_status_type_id .dx-selectbox")
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
            EC.visibility_of_element_located((By.ID, "form-16--1_popup_save-button")))
        ok_btn.click()
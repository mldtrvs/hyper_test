import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class buttonToolbarHelper:
    def __init__(self, app):
        self.app = app

    def click_add_button(self, grid_number):
        css_selector = f"#grid-{grid_number}_tab [role=toolbar] [buttonrole=add]"
        wait = WebDriverWait(self.app.driver, 10)
        add_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
        add_btn.click()
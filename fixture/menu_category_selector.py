from selenium.webdriver.common.by import By

class menuCategorySelectorHelper:

    def __init__(self, app):
        self.app = app

    def go_to_directories(self):
        # Open Directories --> address types menu
        directories_dropdown = self.app.driver.find_element(By.CSS_SELECTOR,
                                                            ".panel-list [role=listbox]>div:nth-child("
                                                            "8)>.dx-list-group-body")
        if not directories_dropdown.is_displayed():
            directories = self.app.driver.find_element(
                By.CSS_SELECTOR, ".panel-list [role=listbox]>div:nth-child(8)>div:first-child")
            directories.click()
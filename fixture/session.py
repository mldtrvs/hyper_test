from selenium.webdriver.common.by import By
import time

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login_HGfilm(self, username, password):
        self.app.open_HGfilm()
        self.app.driver.find_element(By.NAME, "username").send_keys(username)  # login
        self.app.driver.find_element(By.NAME, "password").send_keys(password)  # login
        self.app.driver.find_element(By.CSS_SELECTOR, "#mylsAuthForm [role=button]").click()

    def desktop_projects(self):
        # wait = WebDriverWait(self.app.driver, 10)
        # projects = wait.until(EC.element_to_be_clickable(By.ID, 'buttonDesktop_10'))
        # projects.click()
        self.app.driver.find_element(By.CSS_SELECTOR, '#buttonDesktop_10').click()
        time.sleep(5)

    # def logout_HGfilm(self):
    #     self.app.driver.find_element(By.XPATH, "//div[@class='dx-context-menu-container-border").click()
    #     self.app.driver.find_element(By.XPATH, "//span[@class='dx-menu-item-text']").click()


from selenium.webdriver.common.by import By


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login_HGfilm(self, username, password):
        self.app.open_HGfilm()
        self.app.driver.find_element(By.NAME, "username").send_keys(username)  # login
        self.app.driver.find_element(By.NAME, "password").send_keys(password)  # login
        self.app.driver.find_element(By.XPATH,
                                     "//div[@id='mylsAuthForm']/div/div/div/div[3]/div/div/div/div/span").click()

    # def logout_HGfilm(self):
    #     self.app.driver.find_element(By.XPATH, "//div[@class='dx-context-menu-container-border").click()
    #     self.app.driver.find_element(By.XPATH, "//span[@class='dx-menu-item-text']").click()


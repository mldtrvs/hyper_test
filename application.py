from selenium import webdriver
from selenium.webdriver.common.by import By


def open_HGfilm():
    driver = webdriver.Chrome()
    driver.get("https://hgfilm.ro-zum.eu")
    driver.set_window_size(1124, 894)
    return driver

def login_HGfilm(driver, username, password):
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.XPATH, "//div[@id='mylsAuthForm']/div/div/div/div[3]/div/div/div/div/span").click()
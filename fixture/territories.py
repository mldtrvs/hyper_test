import time

import pytest
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class territoriesHelper:

    def __init__(self, app):
        self.app = app

    def go_to_territories(self):
        wait = WebDriverWait(self.app.driver, 2)
        try:
            positions = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".panel-list a[href='#tree-22_tab']")))
        except TimeoutException:
            self.scroll_menu(wait)
            positions = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".panel-list a[href='#tree-22_tab']")))
        positions.click()
        return wait

    def scroll_menu(self, wait):
        menu_scrollbar = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.panel-list .dx-scrollable-scroll')))
        action_chains = ActionChains(self.app.driver)
        action_chains.move_to_element(menu_scrollbar).perform()
        action_chains.drag_and_drop_by_offset(menu_scrollbar, 0, 164).perform()

    def add_new_rest(self, wait, territory, territory_en, position):
        add_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#tree-22_tab [role=toolbar] ["
                                                                          "buttonrole=add]")))
        add_btn.click()
        self.app.driver.find_element(By.CSS_SELECTOR, "#form-23--1_popup [role=spinbutton]").send_keys(position)
        self.app.driver.find_element(By.CSS_SELECTOR, "#form-23--1_popup [name='territory_name']").send_keys(territory)
        self.app.driver.find_element(
            By.CSS_SELECTOR, "#form-23--1_popup [name='territory_name_en']").send_keys(territory_en)

        ok_btn = wait.until(EC.element_to_be_clickable((By.ID, 'form-23--1_popup_save-button')))
        ok_btn.click()

    def search_for_new_added(self, currency):
        search_input = self.app.driver.find_element(By.CSS_SELECTOR, "#tree-22_tab [role=textbox]")
        search_input.click()
        search_input.clear()
        search_input.send_keys(currency)
        time.sleep(3)
from selenium import webdriver
from fixture.filmType import FilmTypeHelper
from fixture.session import SessionHelper
from fixture.genres import GenresHelper


class Application:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.filmType = FilmTypeHelper(self)
        self.genres = GenresHelper(self)

    def open_HGfilm(self):
        self.driver.get("https://hgfilm.ro-zum.eu")
        self.driver.set_window_size(1124, 894)

    def destroy(self):
        self.driver.quit()

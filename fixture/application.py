from selenium import webdriver

from fixture.addressType import addressTypeHelper
from fixture.ageRestrictions import ageRestrictionHelper
from fixture.documentType import DocumentTypeHelper
from fixture.filmType import FilmTypeHelper
from fixture.session import SessionHelper
from fixture.genres import GenresHelper
from fixture.videoFormat import VideoFormatHelper



class Application:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.session = SessionHelper(self)
        self.filmType = FilmTypeHelper(self)
        self.genres = GenresHelper(self)
        self.videoFormat = VideoFormatHelper(self)
        self.documentType = DocumentTypeHelper(self)
        self.addressType = addressTypeHelper(self)
        self.ageRestrictions = ageRestrictionHelper(self)

    def open_HGfilm(self):
        self.driver.get("https://hgfilm.ro-zum.eu")
        self.driver.set_window_size(1124, 894)

    def destroy(self):
        self.driver.quit()

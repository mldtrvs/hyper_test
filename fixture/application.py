from selenium import webdriver

from fixture.addressType import addressTypeHelper
from fixture.ageRestrictions import ageRestrictionHelper
from fixture.documentType import DocumentTypeHelper
from fixture.filmType import FilmTypeHelper
from fixture.legalForms import legalFormHelper
from fixture.menu_category_selector import menuCategorySelectorHelper
from fixture.session import SessionHelper
from fixture.genres import GenresHelper
from fixture.statuses import statusesHelper
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
        self.legalForms = legalFormHelper(self)
        self.menuCategories = menuCategorySelectorHelper(self)
        self.statuses = statusesHelper(self)

    def open_HGfilm(self):
        self.driver.get("https://hgfilm.ro-zum.eu")
        self.driver.set_window_size(1124, 894)

    def destroy(self):
        self.driver.quit()

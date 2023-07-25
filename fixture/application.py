from selenium import webdriver

from fixture.addressType import addressTypeHelper
from fixture.ageRestrictions import ageRestrictionHelper
from fixture.documentType import DocumentTypeHelper
from fixture.filmType import FilmTypeHelper
from fixture.legalForms import legalFormHelper
from fixture.menu_category_selector import menuCategorySelectorHelper
from fixture.release_type import releaseTypeHelper
from fixture.session import SessionHelper
from fixture.genres import GenresHelper
from fixture.statuses import statusesHelper
from fixture.videoFormat import VideoFormatHelper
from fixture.positions import positionsHelper

class Application:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
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
        self.positions = positionsHelper(self)
        self.releaseType = releaseTypeHelper(self)

    def open_HGfilm(self):
        self.driver.get("https://kino01.id-network.ru/")
        self.driver.set_window_size(1124, 894)
        #self.driver.maximize_window()

    def destroy(self):
        self.driver.quit()

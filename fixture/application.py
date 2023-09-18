from selenium import webdriver

from fixture.addressType import addressTypeHelper
from fixture.ageRestrictions import ageRestrictionHelper
from fixture.currency import currencyHelper
from fixture.documentDetails import docDetailsHelper
from fixture.documentType import DocumentTypeHelper
from fixture.filmType import FilmTypeHelper
from fixture.legalForms import legalFormHelper
from fixture.licenceType import licenceTypeHelper
from fixture.menu_category_selector import menuCategorySelectorHelper
from fixture.personalities import personalitiesHelper
from fixture.personalities_type import personalitiesTypeHelper
from fixture.projects import projectHelper
from fixture.release_type import releaseTypeHelper
from fixture.session import SessionHelper
from fixture.genres import GenresHelper
from fixture.statuses import statusesHelper
from fixture.tags import tagsHelper
from fixture.territories import territoriesHelper
from fixture.videoFormat import VideoFormatHelper
from fixture.positions import positionsHelper


class Application:
    def __init__(self):
        PATH = "C:/Program Files (x86)/chromedriver.exe"
        self.driver = webdriver.Chrome(PATH)
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
        self.tags = tagsHelper(self)
        self.personalitiesType = personalitiesTypeHelper(self)
        self.personalities = personalitiesHelper(self)
        self.licenceType = licenceTypeHelper(self)
        self.docDetails = docDetailsHelper(self)
        self.currency = currencyHelper(self)
        self.territories = territoriesHelper(self)
        self.projects = projectHelper(self)

    def open_HGfilm(self):
        self.driver.get("https://kino01.id-network.ru/")
        #self.driver.set_window_size(1124, 894)
        self.driver.maximize_window()

    def destroy(self):
        self.driver.quit()

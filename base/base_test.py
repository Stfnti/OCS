import pytest

from pages.landing_page import LandingPage
from pages.landing_english_page import LandingEnglishPage
from components.header import Header

class BaseTest:

    landing_page: LandingPage
    landing_english_page: LandingEnglishPage
    header: Header

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.landing_page = LandingPage(driver)
        request.cls.landing_english_page = LandingEnglishPage(driver)
        request.cls.header = Header(driver)

import allure

from base.base_page import BasePage
from config.links import Links

from selenium.webdriver.support import expected_conditions as EC

class LandingEnglishPage(BasePage):

    PAGE_URL = Links.LANDING_ENGLISH_PAGE

    TITLE = "xpath", "//h1"

    @allure.title("Get page title")
    def get_page_title(self) -> str:
        """Get page title."""
        title_element = self.wait.until(EC.visibility_of_element_located(self.TITLE))
        return title_element.text
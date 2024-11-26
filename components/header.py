import allure

from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class Header(BasePage):

    IN_ENGLISH = "xpath", "//a[@class='link' and contains(text(), 'In English')]"
    LOGIN = "xpath", "//a[contains(text(), 'Войти') and contains(@class, 'btn')]"
    BECOME_PARTNER = "xpath", "//a[contains(text(), 'Стать партнером') and contains(@class, 'btn-xs')]"

    def click_login_button(self) -> None:
        """Click button 'ВОЙТИ'."""
        self.wait.until(EC.element_to_be_clickable(self.LOGIN)).click()

    def click_become_partner_button(self) -> None:
        """Click button 'СТАТЬ ПАРТНЕРОМ'."""
        self.wait.until(EC.element_to_be_clickable(self.BECOME_PARTNER)).click()

    @allure.title("Click 'In English' button")
    def click_in_english_button(self) -> None:
        """Click button 'In English'."""
        self.wait.until(EC.element_to_be_clickable(self.IN_ENGLISH)).click()
import allure
from assertpy import assert_that

from base.base_test import BaseTest


class TestHeader(BaseTest):

    @allure.title("Test Login Button Works Correctly")
    def test_in_english_button_work_correctly(self):
        self.landing_page.open()
        self.header.click_in_english_button()
        assert_that(self.landing_english_page.get_page_title()).is_equal_to("In English")
import time


import pytest

from pages.ReviewPage import ReviewPage
from pages.LoginPage import LoginPage

class Test3:

    #@pytest.fixture()
    @pytest.mark.parametrize('all_browser', ['chrome'])
    def test_review_product(self, run_all_browser, all_browser):
        home_page = run_all_browser
        login_page = LoginPage(driver=home_page.driver)
        login_page.login('teste1@teste.com', '1234567a')
        review_page = ReviewPage(driver=home_page.driver)
        review_page.fill_review_title("Titulo da Review")
        review_page.fill_review_text("O produto é ótimo, recomendo")
        review_page.fill_review_note()
        review_page.click_review_button()
        assert review_page.has_review_success_message('Product review is successfully added.')
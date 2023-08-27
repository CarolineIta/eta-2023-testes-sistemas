import pytest
from selenium.webdriver.support.wait import WebDriverWait

from pages.BooksPage import BooksPage
from pages.HomePage import HomePage


class Test6:

    #@pytest.fixture()
    @pytest.mark.parametrize('all_browser', ['chrome'])
    def test_order_price(self, run_all_browser, all_browser):
        home_page = run_all_browser
        home_page.click_books_menu()
        books_page = BooksPage(driver=home_page.driver)
        books_page.filter_by_price_low_to_high()
        assert books_page.check_order_by_price_low_to_high()
        home_page.close_browser()
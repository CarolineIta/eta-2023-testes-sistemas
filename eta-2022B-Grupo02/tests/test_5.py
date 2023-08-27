import time
from lib2to3.pgen2 import driver

import pytest
from selenium.webdriver.support.wait import WebDriverWait

from pages.HomePage import HomePage


class Test5:

    #@pytest.fixture()
    @pytest.mark.parametrize('all_browser', ['chrome'])
    def test_subscribe_newsletter(self, run_all_browser, all_browser):
        home_page = run_all_browser
        home_page.fill_newsletter("teste@teste.com")
        assert home_page.has_newsletter_subscribe()
        home_page.close_browser()
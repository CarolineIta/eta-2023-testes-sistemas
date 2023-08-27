import time
from lib2to3.pgen2 import driver

import pytest
from selenium.webdriver.support.wait import WebDriverWait

from pages.HomePage import HomePage


class Test1:

    #@pytest.fixture()
    @pytest.mark.parametrize('all_browser', ['chrome'])
    def test_add_product_to_cart(self, run_all_browser, all_browser):
        home_page = run_all_browser
        home_page.fill_search_product('Computing and Internet')
        home_page.click_search_btn()
        assert home_page.has_title('Computing and Internet'), 'Produto não encontrado'
        home_page.click_add_to_cart_btn()
        assert home_page.has_product(),'Produto não encontrado'
        home_page.close_browser()







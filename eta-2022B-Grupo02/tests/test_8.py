import time
from lib2to3.pgen2 import driver

import pytest
from selenium.webdriver.support.wait import WebDriverWait

from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from pages.ProductsDetailsPage import ProductsDetailsPage


class Test8:

    #@pytest.fixture()
    @pytest.mark.parametrize('all_browser', ['chrome'])
    def test_checkout(self, run_all_browser, all_browser):
        home_page = run_all_browser
        login_page = LoginPage(driver=home_page.driver)
        login_page.login('teste1@teste.com', '1234567a')
        home_page.fill_search_product('Computing and Internet')
        home_page.click_search_btn()
        home_page.click_add_to_cart_btn()
        products_details_page = ProductsDetailsPage(driver=home_page.driver)
        products_details_page.click_link_go_to_cart()
        products_details_page.select_country()
        products_details_page.fill_zipcode_field("11320180")
        products_details_page.click_estimate_shipping_button()
        products_details_page.click_agree_terms_check()
        products_details_page.click_checkout_button()
        assert products_details_page.has_checkout_title()
        home_page.close_browser()
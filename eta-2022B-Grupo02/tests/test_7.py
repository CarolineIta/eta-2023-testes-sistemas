import time
from lib2to3.pgen2 import driver


import pytest
from selenium.webdriver.support.wait import WebDriverWait

from pages.CustomerPage import CustomerPage
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage


class Test7:

    #@pytest.fixture()
    @pytest.mark.parametrize('all_browser', ['chrome'])
    def test_change_password(self, run_all_browser, all_browser):
        home_page = run_all_browser
        login_page = LoginPage(driver=home_page.driver)
        login_page.login('teste1@teste.com', '1234567a')
        home_page.click_my_account()
        customer_page = CustomerPage(driver=home_page.driver)
        customer_page.click_change_password_link()
        customer_page.fill_password_fields("1234567a","1234567a","1234567a")
        assert customer_page.has_password_success_message()
        home_page.close_browser()
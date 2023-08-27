import time
from lib2to3.pgen2 import driver

import pytest
from selenium.webdriver.support.wait import WebDriverWait

from pages.HomePage import HomePage
from pages.LoginPage import LoginPage


class Test9:

    #@pytest.fixture()
    @pytest.mark.parametrize('all_browser', ['chrome'])
    def test_recovery_password(self, run_all_browser, all_browser):
        home_page = run_all_browser
        home_page.click_login_link()
        login_page = LoginPage(driver=home_page.driver)
        login_page.click_forgot_password()
        login_page.fill_email_to_recovery_pass('teste1@teste.com')
        login_page.click_send_recovery_email()
        assert login_page.has_email_send_message()
        home_page.close_browser()
import time
from lib2to3.pgen2 import driver

import pytest
from selenium.webdriver.support.wait import WebDriverWait

from pages.HomePage import HomePage
from pages.RegisterPage import RegisterPage

class Test2:

    #@pytest.fixture()
    @pytest.mark.parametrize('all_browser', ['chrome'])
    def test_register_new_user(self, run_all_browser, all_browser):
        home_page = run_all_browser
        home_page.click_register_btn()
        register_page = RegisterPage(driver=home_page.driver)
        register_page.fill_gender()
        register_page.fill_first_name('Amanda')
        register_page.fill_last_name('Silva')
        register_page.fill_email()
        register_page.fill_password('1234567a')
        register_page.fill_confirm_password('1234567a')
        register_page.click_register_btn()
        assert register_page.has_register_message('Your registration completed'), 'Mensagem não encontrada'
import time
from lib2to3.pgen2 import driver

import pytest
from selenium.webdriver.support.wait import WebDriverWait

from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from pages.ProductEmailFriendPage import ProductsEmailFriendPage

class Test4:

    #@pytest.fixture()
    @pytest.mark.parametrize('all_browser', ['chrome'])
    def test_send_email_to_friend(self, run_all_browser, all_browser):
        home_page = run_all_browser
        login_page = LoginPage(driver=home_page.driver)
        login_page.login('teste1@teste.com', '1234567a')
        email_page = ProductsEmailFriendPage(driver=home_page.driver)
        email_page.fill_friend_email("friend@teste.com")
        email_page.fill_personal_message("Olhei esse produto e lembrei de você")
        email_page.click_send_email_to_friend()
        assert email_page.has_send_email_success_message("Your message has been sent.")
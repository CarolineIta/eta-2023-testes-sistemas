import time
from lib2to3.pgen2 import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.PageObject import PageObject


class HomePage(PageObject):
    url = 'https://demowebshop.tricentis.com/'
    id_search_store = 'small-searchterms'
    css_search_btn = '[value="Search"]'
    class_title_product = 'product-title'
    css_add_to_cart_btn = '[value="Add to cart"]'
    class_go_to_cart = 'cart-label'
    qtd_cart = 'cart-qty'
    link_register = '.ico-register'
    id_newsletter_email = 'newsletter-email'
    id_newsletter_button = 'newsletter-subscribe-button'
    class_message_newsletter = 'newsletter-result-block'
    link_login_page = 'ico-login'
    link_my_account = 'My account'
    link_books_menu = 'Books'

    def __init__(self, browser):
        super(HomePage, self).__init__(browser=browser)
        self.driver.get(self.url)

    def fill_search_product(self, product):
        self.driver.find_element(By.ID, self.id_search_store).send_keys(product)

    def click_search_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_search_btn).click()

    def has_title(self, product_name):
        title_page = self.driver.find_element(By.CLASS_NAME, self.class_title_product).text
        return title_page == product_name

    def click_add_to_cart_btn(self):
       self.driver.find_element(By.CSS_SELECTOR, self.css_add_to_cart_btn).click()

    def has_product(self):
        quantidade_produtos = self.driver.find_element(By.CLASS_NAME, self.qtd_cart)
        return quantidade_produtos != 0

    def click_register_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, self.link_register).click()

    def fill_newsletter(self, email):
        self.driver.find_element(By.ID, self.id_newsletter_email).send_keys(email)
        self.driver.find_element(By.ID, self.id_newsletter_button).click()

    def has_newsletter_subscribe(self):
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, self.class_message_newsletter),
                                             "Thank you for signing up! A verification email has been sent. We appreciate your interest.")
        )
        return True

    def click_login_link(self):
        self.driver.find_element(By.CLASS_NAME, self.link_login_page).click()

    def click_my_account(self):
       self.driver.find_element(By.CLASS_NAME, self.link_my_account).click()

    def click_books_menu(self):
        self.driver.find_element(By.LINK_TEXT, self.link_books_menu).click()

    def click_my_account(self):
        self.driver.find_element(By.LINK_TEXT, self.link_my_account).click()

    def close_browser(self):
       self.driver.quit()















    # def has_login_error_message(self):
    #     error_message = self.driver.find_element(By.CSS_SELECTOR, self.login_error_message).text
    #     return error_message == self.txt_login_error_message
    #
    # def efetuar_login(self, user_name='standard_user', password='secret_sauce'):
    #     self.driver.find_element(By.ID, self.id_username).send_keys(user_name)
    #     self.driver.find_element(By.ID, self.id_password).send_keys(password)
    #     self.click_login_btn()

import time

from selenium.webdriver.common.by import By
from pages.PageObject import PageObject


class LoginPage(PageObject):
    url = 'https://demowebshop.tricentis.com/login'
    id_email = 'Email'
    id_password = 'Password'
    css_btn_login = '[value="Log in"]'
    link_forgot_password = 'Forgot password?'
    class_email_to_recovery_pass = 'email'
    css_recovery_email_button = '[value="Recover"]'
    class_message_email_send = 'result'

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver=driver)
        self.driver.get(self.url)

    def login(self, email, password):
        self.driver.find_element(By.ID, self.id_email).send_keys(email)
        self.driver.find_element(By.ID, self.id_password).send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, self.css_btn_login).click()

    def click_forgot_password(self):
        self.driver.find_element(By.LINK_TEXT, self.link_forgot_password).click()

    def fill_email_to_recovery_pass(self, email):
        self.driver.find_element(By.CLASS_NAME, self.class_email_to_recovery_pass).send_keys(email)

    def click_send_recovery_email(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_recovery_email_button).click()

    def has_email_send_message(self):
        message_success = self.driver.find_element(By.CLASS_NAME, self.class_message_email_send).text
        return message_success == 'Email with instructions has been sent to you.'
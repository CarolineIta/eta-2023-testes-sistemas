import time

from selenium.webdriver.common.by import By
from pages.PageObject import PageObject
import random
import string


class RegisterPage(PageObject):
    url = 'https://demowebshop.tricentis.com/register'
    id_genero_register = 'gender-female'
    id_first_name = 'FirstName'
    id_last_name = 'LastName'
    id_email = 'Email'
    id_password = 'Password'
    id_confirm_password = 'ConfirmPassword'
    id_register_button = 'register-button'
    class_registration_message = 'result'
    button_continue = '.button-1 register-continue-button'

    def __init__(self, driver):
        super(RegisterPage, self).__init__(driver=driver)

    def fill_gender(self):
        self.driver.find_element(By.ID, self.id_genero_register).click()

    def fill_first_name(self, firstname):
         self.driver.find_element(By.ID, self.id_first_name).send_keys(firstname)

    def fill_last_name(self, lastname):
         self.driver.find_element(By.ID, self.id_last_name).send_keys(lastname)

    def fill_email(self):
        random_email = self.generate_random_email()
        self.driver.find_element(By.ID, self.id_email).send_keys(random_email)

    def generate_random_email(self):
        domains = ["gmail.com", "yahoo.com", "outlook.com"]
        username = ''.join(
            random.choice(string.ascii_letters) for _ in range(8))
        domain = random.choice(domains)
        email = f"{username}@{domain}"
        return email

    def fill_password(self, password):
         self.driver.find_element(By.ID, self.id_password).send_keys(password)

    def fill_confirm_password(self, confirm_password):
        self.driver.find_element(By.ID, self.id_confirm_password).send_keys(confirm_password)

    def click_register_btn(self):
         self.driver.find_element(By.ID, self.id_register_button).click()

    def has_register_message(self, title_text):
        message_register = self.driver.find_element(By.CLASS_NAME, self.class_registration_message).text
        return message_register == title_text


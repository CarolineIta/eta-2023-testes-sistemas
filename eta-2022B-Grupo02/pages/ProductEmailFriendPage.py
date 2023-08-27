from selenium.webdriver.common.by import By
from pages.PageObject import PageObject


class ProductsEmailFriendPage(PageObject):
    url = 'https://demowebshop.tricentis.com/productemailafriend/13'
    id_friend_email = 'FriendEmail'
    id_personal_message = 'PersonalMessage'
    text_link_send_email = 'button-2 email-a-friend-button'
    css_send_email_button = '[value="Send email"]'
    class_message_send_email = 'result'

    def __init__(self, driver):
        super(ProductsEmailFriendPage, self).__init__(driver=driver)
        self.driver.get(self.url)

    def fill_friend_email(self, friend_email):
        self.driver.find_element(By.ID, self.id_friend_email).send_keys(friend_email)

    def fill_personal_message(self, message):
        self.driver.find_element(By.ID, self.id_personal_message).send_keys(message)

    def click_send_email_to_friend(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_send_email_button).click()

    def has_send_email_success_message(self, message_text):
        message_email_success = self.driver.find_element(By.CLASS_NAME, self.class_message_send_email).text
        return message_email_success == message_text


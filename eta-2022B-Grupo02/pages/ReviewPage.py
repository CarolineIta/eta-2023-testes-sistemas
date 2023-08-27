from selenium.webdriver.common.by import By
from pages.PageObject import PageObject


class ReviewPage(PageObject):
    url = 'https://demowebshop.tricentis.com/productreviews/13'
    id_review_title = 'AddProductReview_Title'
    id_review_text = 'AddProductReview_ReviewText'
    id_excelent_review = 'addproductrating_5'
    css_btn_login = '[value="Log in"]'
    css_review_button = '[value="Submit review"]'
    class_review_success = 'result'


    def __init__(self, driver):
        super(ReviewPage, self).__init__(driver=driver)
        self.driver.get(self.url)

    def fill_review_title(self, review_title):
        self.driver.find_element(By.ID, self.id_review_title).send_keys(review_title)

    def fill_review_text(self, review_text):
        self.driver.find_element(By.ID, self.id_review_text).send_keys(review_text)

    def fill_review_note(self):
        self.driver.find_element(By.ID, self.id_excelent_review).click()

    def click_review_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_review_button).click()

    def has_review_success_message(self, message_text):
        message_review = self.driver.find_element(By.CLASS_NAME, self.class_review_success).text
        return message_review == message_text


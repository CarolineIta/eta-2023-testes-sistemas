from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.PageObject import PageObject


class ProductsDetailsPage(PageObject):
    url = 'https://demowebshop.tricentis.com/computing-and-internet'
    id_genero_register = 'gender-female'
    text_link_review = 'Add your review'
    text_link_send_email = 'button-2 email-a-friend-button'
    link_go_to_cart = 'Shopping cart'
    class_car_icon = 'ico-cart'
    id_filter_select = 'CountryId'
    value_country = '17'
    class_zipcode_field = 'zip-input'
    css_estimate_shipping_button = '[value="Estimate shipping"]'
    class_estimate_shipping_result = 'option-name'
    id_termofservice = 'termsofservice'
    id_checkout_button = 'checkout'
    class_checkout_title = 'page-title'




    def _init_(self, driver):
        super(ProductsDetailsPage, self)._init_(driver=driver)
        self.driver.get(self.url)

    def click_review_link(self):
        self.driver.find_element(By.LINK_TEXT, self.text_link_review).click()

    def click_send_email_link(self):
        self.driver.find_element(By.LINK_TEXT, self.text_link_send_email).click()

    def click_link_go_to_cart(self):
        self.driver.find_element(By.LINK_TEXT, self.link_go_to_cart).click()

    def click_go_to_car_link(self):
        self.driver.find_element(By.CLASS_NAME, self.class_car_icon).click()

    def select_country(self):
        select_element = self.driver.find_element(By.ID, self.id_filter_select)
        select = Select(select_element)
        select.select_by_value(self.value_country)

    def fill_zipcode_field(self, zipcode):
        self.driver.find_element(By.CLASS_NAME, self.class_zipcode_field).send_keys(zipcode)

    def click_estimate_shipping_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_estimate_shipping_button).click()

    def has_shipping_estimate(self, message_text):
        # shipping_estimate = self.driver.find_element(By.CLASS_NAME, self.class_estimate_shipping_result).text
        # return shipping_estimate != ""

        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, self.class_estimate_shipping_result),
                                             "Ground")
        )
        return True

    def click_agree_terms_check(self):
        self.driver.find_element(By.ID, self.id_termofservice).click()

    def click_checkout_button(self):
        self.driver.find_element(By.ID, self.id_checkout_button).click()

    def has_checkout_title(self):
        checkout_title = self.driver.find_element(By.CLASS_NAME, self.class_checkout_title).text
        return checkout_title == "Checkout"
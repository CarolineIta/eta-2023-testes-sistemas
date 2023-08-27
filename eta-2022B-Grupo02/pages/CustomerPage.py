from selenium.webdriver.common.by import By
from pages.PageObject import PageObject
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CustomerPage(PageObject):
    url = 'https://demowebshop.tricentis.com/customer/info'
    link_change_password_link = 'Change password'
    id_old_password_field = 'OldPassword'
    id_new_password_field = 'NewPassword'
    id_confirm_password_field = 'ConfirmNewPassword'
    css_change_password_btn = '[value="Change password"]'
    class_result_password_changed_message = 'result'


    def _init_(self, driver):
        super(CustomerPage, self)._init_(driver=driver)
        self.driver.get(self.url)

    def click_change_password_link(self):
        self.driver.find_element(By.LINK_TEXT, self.link_change_password_link).click()

    def fill_password_fields(self, oldpass , newpass , confpass):
        self.driver.find_element(By.ID, self.id_old_password_field).send_keys(oldpass)
        self.driver.find_element(By.ID, self.id_new_password_field).send_keys(newpass)
        self.driver.find_element(By.ID, self.id_confirm_password_field).send_keys(confpass)
        self.driver.find_element(By.CSS_SELECTOR, self.css_change_password_btn).click()

    def has_password_success_message(self):
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, self.class_result_password_changed_message),
                                             "Password was changed")
        )
        return True
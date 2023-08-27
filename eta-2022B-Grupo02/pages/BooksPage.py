from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.PageObject import PageObject


class BooksPage(PageObject):
    url = 'https://demowebshop.tricentis.com/books'
    id_filter_select = 'products-orderby'
    value_low_high = 'https://demowebshop.tricentis.com/books?orderby=10'
    class_item_price = '[class="price actual-price"]'



    def _init_(self, driver):
        super(BooksPage, self)._init_(driver=driver)


    def filter_by_price_low_to_high(self):
        select_element = self.driver.find_element(By.ID, self.id_filter_select)
        select = Select(select_element)
        select.select_by_value(self.value_low_high)


    def check_order_by_price_low_to_high(self):
        all_price_items = self.driver.find_elements(By.CSS_SELECTOR, self.class_item_price)

        for i in range(len(all_price_items) - 1):
            current_price = float(all_price_items[i].text.replace('$', ''))
            next_price = float(all_price_items[i + 1].text.replace('$', ''))
            print(f'Current prince: {current_price}')
            print(f'Next prince: {next_price}')
            print('-----------------------------')
            if current_price > next_price:
                return False
        return True
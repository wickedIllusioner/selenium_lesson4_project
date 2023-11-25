from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from .locators import ProductPageLocators
import math


class ProductPage(BasePage):

    def product_page_test(self):
        self.click_add_to_basket_btn()
        self.solve_quiz_and_get_code()
        self.book_price_should_be_equal_to_basket_total()
        self.check_accuracy_of_book_title()
        

    def click_add_to_basket_btn(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_btn.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
    
    def book_price_should_be_equal_to_basket_total(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text.split()[2]

        print(f'Basket total is: {basket_total}')
        assert basket_total == book_price, 'Basket total is not equal to given book price'
        
    def check_accuracy_of_book_title(self):
        book_title = self.browser.find_element(*ProductPageLocators.BOOK_TITLE).text.split('\n')[0]
        alertinner_text = self.browser.find_element(*ProductPageLocators.INNER_ALERT_BOOK_TITLE).text

        assert book_title == alertinner_text, 'Book titles do not match'


    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"
    
    def success_message_should_be_absent(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), 'Success message is still present'

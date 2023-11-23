from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    
    def basket_should_be_empty(self):
        self.no_items_in_basket_list()
        self.basket_empty_message_should_be_present()


    def no_items_in_basket_list(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEM_LIST), 'Item list is not empty'
    
    def basket_empty_message_should_be_present(self):
        assert 'Your basket is empty.' in self.browser.find_element(*BasketPageLocators.INNER_BASKET_MESSAGE).text, 'No basket empty message'
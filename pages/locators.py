from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')

class ProductPageLocators():
    ADD_TO_BASKET = (By.CLASS_NAME, 'btn-add-to-basket')
    BASKET_TOTAL = (By.CLASS_NAME, 'basket-mini')
    BOOK_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    BOOK_TITLE = (By.CLASS_NAME, 'product_main')
    INNER_ALERT_BOOK_TITLE = (By.CSS_SELECTOR, '#messages strong')
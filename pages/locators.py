from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    BASKET_BUTTON = (By.CSS_SELECTOR, '.basket-mini a.btn')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')

    REGISTER_EMAIL = (By.ID, 'id_registration-email')
    REGISTER_PASSWORD = (By.ID, 'id_registration-password1')
    REGISTER_CONFIRM_PASSWORD = (By.ID, 'id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"]')

class ProductPageLocators():
    ADD_TO_BASKET = (By.CLASS_NAME, 'btn-add-to-basket')
    BASKET_TOTAL = (By.CLASS_NAME, 'basket-mini')
    BOOK_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    BOOK_TITLE = (By.CLASS_NAME, 'product_main')
    INNER_ALERT_BOOK_TITLE = (By.CSS_SELECTOR, '#messages strong')
    SUCCESS_MESSAGE = (By.CLASS_NAME, 'alert-success')

class BasketPageLocators():
    ITEM_LIST = (By.CLASS_NAME, 'basket-items')
    INNER_BASKET_MESSAGE = (By.CSS_SELECTOR, '#content_inner')
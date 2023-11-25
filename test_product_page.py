from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
link2 = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
link3 = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'


@pytest.mark.need_review
@pytest.mark.parametrize('promo_offer', [x for x in range(10)])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()

    page.product_page_test()


class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        self.link = 'http://selenium1py.pythonanywhere.com'

        self.login_page = LoginPage(browser, self.link)
        self.login_page.open()
        self.login_page.go_to_login_page()

        self.generated_data = self.login_page.generate_email_and_password()
        self.email = self.generated_data[0]
        self.password = self.generated_data[1]
        self.login_page.register_new_user(self.email, self.password)

        self.login_page.should_be_authorized()


    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()

        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link3)
        page.open()

        page.product_page_test()




@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product(browser):
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket_btn()
    
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()

    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket_btn()

    page.success_message_should_be_absent()



def test_guest_can_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, link2)
    page.open()
    page.go_to_basket_page()
    page.basket_should_be_empty()
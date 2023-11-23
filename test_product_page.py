from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.locators import ProductPageLocators
import pytest


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
link2 = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'

# @pytest.mark.parametrize('promo_offer', [x for x in range(10)])
# def test_guest_can_add_product_to_basket(browser, promo_offer):
#     link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
#     page = ProductPage(browser, link)
#     page.open()

#     page.product_page_test()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product(browser):
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket_btn()
    
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), 'Success message is present'

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()

    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), 'Success message is present'

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket_btn()

    assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), 'Success message is still present'




def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_should_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, link2)
    page.open()
    page.go_to_basket_page()
    page.basket_should_be_empty()
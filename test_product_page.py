from .pages.product_page import ProductPage
import pytest


@pytest.mark.parametrize('promo_offer', [x for x in range(10)])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()

    page.product_page_test()
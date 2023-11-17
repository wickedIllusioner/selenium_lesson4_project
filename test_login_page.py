from .pages.locators import MainPageLocators
from .pages.login_page import LoginPage
from .pages.main_page import MainPage


link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_register_and_login_forms(browser):
    # Инициализация страницы в теле теста, переход неявный
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
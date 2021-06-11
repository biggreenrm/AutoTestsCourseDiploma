#firstparty
from .pages.login_page import LoginPage


link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

def test_should_be_login_page(browser):
    page = LoginPage(browser, link)
    page.open()
    
    page.should_be_login_page()
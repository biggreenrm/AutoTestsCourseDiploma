#firstparty
from .pages.product_page import ProductPage
from .constants import SET_OF_PRODUCT_LINKS
import time

#thirdparty
import pytest
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


# @pytest.mark.parametrize("link", SET_OF_PRODUCT_LINKS)
# def test_guest_can_add_product_to_basket(browser, link):
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_product_to_basket()
#     page.solve_quiz_and_get_code()
#     page.should_be_equal_basket_total_and_price()
#     page.should_be_equal_product_name_and_in_basket()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_present_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_present_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_disappear_success_message()

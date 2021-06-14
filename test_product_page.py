#firstparty
from .pages.product_page import ProductPage
from .constants import SET_OF_PRODUCT_LINKS
import time

#thirdparty
import pytest


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


@pytest.mark.parametrize("link", SET_OF_PRODUCT_LINKS)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_equal_basket_total_and_price()
    page.should_be_equal_product_name_and_in_basket()

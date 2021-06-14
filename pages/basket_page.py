#firstparty
from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    
    def should_be_no_products(self):
        products = self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET)
        assert products

    def should_be_empty_basket_message(self):
        basket_message = self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE)
        assert basket_message
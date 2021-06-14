#firstparty
from .base_page import BasePage
from .locators import ProductPageLocators

#thirdparty
from selenium.webdriver.common.by import By


class ProductPage(BasePage):

    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()
    
    def should_be_equal_basket_total_and_price(self):
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert basket_total == price, "Price of product and basket total is not equal"
    
    def should_be_equal_product_name_and_in_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_AFTER_ADD_TO_BASKET).text
        assert product_name == product_name_in_basket, "Product names on page and in basket is not equal"

from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_not_be_products_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Basket is not empty, but should"

    def should_be_message_about_empty_basket(self):
        assert "Your basket is empty." in self.get_element_text(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "There is no message or it is incorrect"
        # Проверка только на английский язык пройдёт, но можно и на другие потом проверить
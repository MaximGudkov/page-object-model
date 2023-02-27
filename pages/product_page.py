from .base_page import BasePage
from .locators import ProductPageLocators as PPLocs


class ProductPage(BasePage):

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*PPLocs.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*PPLocs.SUCCESS_MESSAGE),\
            "Success message is not disappeared"

    def adding_to_basket(self):
        self.browser.find_element(*PPLocs.ADD_INTO_BASKET_BUTTON).click()
        # self.solve_quiz_and_get_code()

    def __compare_elements_texts(self, locator1: tuple, locator2: tuple) -> bool:
        return self.get_element_text(*locator1) == self.get_element_text(*locator2)

    def should_have_correct_product_name_after_added_in_basket(self):
        assert self.is_element_present(*PPLocs.ADDED_IN_BASKET_MESSAGE), 'there is no name of the product message'
        assert self.__compare_elements_texts(PPLocs.PRODUCT_NAME, PPLocs.PRODUCT_NAME_IN_MESSAGE), 'names are not same'

    def should_have_correct_product_price_after_added_in_basket(self):
        assert self.is_element_present(*PPLocs.PRICE_OF_BASCET_MESSAGE), 'there is no price of the product message'
        assert self.__compare_elements_texts(PPLocs.PRODUCT_PRICE, PPLocs.BASCET_PRICE), 'prices are not the same'




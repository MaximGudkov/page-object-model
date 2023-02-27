from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators:
    ADD_INTO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success:first-child")

    ADDED_IN_BASKET_MESSAGE = (By.CLASS_NAME, "alertinner")
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, ".alert-success strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")

    PRICE_OF_BASCET_MESSAGE = (By.CLASS_NAME, "alert-info")
    BASCET_PRICE = (By.CSS_SELECTOR, ".alert-info strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

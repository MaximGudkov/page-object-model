import time
import pytest

from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

PRODUCT_DESCRIPTION_LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, PRODUCT_DESCRIPTION_LINK, timeout=0)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, PRODUCT_DESCRIPTION_LINK)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_products_in_basket()
    basket_page.should_be_message_about_empty_basket()


@pytest.mark.login_guest
class TestLoginFromProductPage:

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, PRODUCT_DESCRIPTION_LINK)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()


@pytest.mark.guest_add_to_basket
class TestGuestAddToBasketFromProductPage:

    # @pytest.mark.parametrize('n', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser):
        # link = PRODUCT_DESCRIPTION_LINK + f"?promo=offer{n}"
        page = ProductPage(browser, PRODUCT_DESCRIPTION_LINK)
        page.open()
        page.adding_to_basket()
        page.should_have_correct_product_name_after_added_in_basket()
        page.should_have_correct_product_price_after_added_in_basket()

    @pytest.mark.xfail(reason="it is a fail test yet")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, PRODUCT_DESCRIPTION_LINK, timeout=0)
        page.open()
        page.adding_to_basket()
        page.should_not_be_success_message()

    @pytest.mark.xfail(reason="we know that the message will not disappear")
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, PRODUCT_DESCRIPTION_LINK, timeout=0)
        page.open()
        page.adding_to_basket()
        page.should_dissapear_of_success_message()


@pytest.mark.user_add_to_basket
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        login_page = LoginPage(browser, link)
        login_page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, PRODUCT_DESCRIPTION_LINK, timeout=0)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, PRODUCT_DESCRIPTION_LINK)
        page.open()
        page.adding_to_basket()
        page.should_have_correct_product_name_after_added_in_basket()
        page.should_have_correct_product_price_after_added_in_basket()

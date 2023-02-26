from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.adding_to_basket()
    page.should_have_correct_product_name_after_added_in_basket()
    page.should_have_correct_product_price_after_added_in_basket()


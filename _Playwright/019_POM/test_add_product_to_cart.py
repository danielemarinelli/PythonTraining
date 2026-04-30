import pytest
from playwright.sync_api import expect, Page
from loginpage import LoginPage
from myaccount import MyAccount
from cartpage import CartPage

@pytest.mark.parametrize("username, password, product_name", [
    ("pavanol", "test@123", "Nokia lumia 1520"),
    ("pavanol", "test@123", "Sony vaio i5")
])
def test_user_can_login_and_add_product_to_cart(page: Page, username, password, product_name):
    # Navigate to site
    page.goto("https://www.demoblaze.com/index.html")

    # --- Login Page ---
    # click on login button and insert credentials
    login_page = LoginPage(page)  # create object
    login_page.click_login_link()
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login_button()

    # --- MyAccount ---
    # select the product from the list and it to the cart and navigate to cart
    my_account = MyAccount(page)  # create object
    my_account.add_product_to_cart(product_name)
    page.wait_for_timeout(3000)
    my_account.goto_cart()
    page.wait_for_timeout(3000)

    # --- Cart Page ---
    #check that the product selected is visible in the cart
    cart_page = CartPage(page)  # create object
    product_in_cart = cart_page.check_product_in_cart(product_name)

    # validation
    expect(product_in_cart).to_be_visible()

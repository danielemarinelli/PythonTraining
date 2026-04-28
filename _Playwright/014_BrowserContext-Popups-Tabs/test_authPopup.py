from playwright.sync_api import expect, Playwright, Page
import pytest

#Direct - inject user login with url

# https://the-internet.herokuapp.com/basic_auth -->> POP UP WILL ASK USER & PW

#https://admin:admin@the-internet.herokuapp.com/basic_auth

@pytest.mark.skip
def test_authPopup(page:Page):
    # inserted username & pw directly in the URL (not best practice)
    # did not follow any context approach
    page.goto("https://admin:admin@the-internet.herokuapp.com/basic_auth")
    page.wait_for_load_state()
    expect(page.locator("text=Congratulations")).to_be_visible()
    page.wait_for_timeout(3000)


# using context - we can pass user and password along with the context
# to use context we need 'playwright' feature
def test_authPopup_context(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context(
        http_credentials={"username":"admin","password":"admin"}  # must pass credentials in the context as <k,v> pair
    )
    page=context.new_page()

    page.goto("https://the-internet.herokuapp.com/basic_auth")
    page.wait_for_load_state()
    expect(page.locator("text=Congratulations")).to_be_visible()
    page.wait_for_timeout(5000)
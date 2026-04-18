# pytest _Playwright/002_Locators/test_locators.py -v -s --headed
# BUILD-IN LOCATORS IN PLAYWRIGHT:
# 1) page.get_by_alt_text() --> Locate images by their alt attribute
# 2) page.get_by_text() --> Locate by visible text content


from playwright.sync_api import Page, expect

def test_verify_playwrightLocators(page: Page):
    page.goto("https://demo.nopcommerce.com/")
    page.wait_for_timeout(2000)
    # 1)
    logo=page.get_by_alt_text("nopCommerce demo store")  # inspecting the logo , img has the alt text , so we can use the  get_by_alt_text()
    expect(logo).to_be_visible()
    #2)
    expect(page.get_by_text("Featured products")).to_be_visible()
    expect(page.get_by_text("Welcome to our store")).to_be_visible()



from playwright.sync_api import sync_playwright, expect, Page, Playwright


'''
Browser ----> chromium, firefox, webkit etc.....
page --> tab, popup, window
Browser --->context (user profiles)----> pages
'''

# we must use feature named ---> playwright from class Playwright
def test_browser_context(playwright:Playwright):
    # chromium=playwright.chromium
    # browser=chromium.launch()   # by default headless is 'True'

    browser=playwright.chromium.launch(headless=False)  # created browser and at this level we need to specify the headed mode or not
    context=browser.new_context() # created context

    page1=context.new_page()  # created page1
    page2 = context.new_page()  # created page2
    # we can work in parallel with multiple web pages:
    # for multiple pages we need context feature
    page1.goto("https://playwright.dev/")
    page1.wait_for_timeout(2000)
    expect(page1).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright")

    page2.goto("https://www.selenium.dev/")
    page2.wait_for_timeout(2000)
    expect(page2).to_have_title("Selenium")
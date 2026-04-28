from playwright.sync_api import sync_playwright, expect, Playwright

def test_handle_popups(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()

    page.goto("https://testautomationpractice.blogspot.com/")
    # REGISTER the EVENT named 'popup' to handle the pop-ups
    # def handle_popup(popup):
    #     popup.wait_for_load_state()
    #
    # page.on("popup",handle_popup)

    page.on("popup",lambda popup:popup.wait_for_load_state())
    # Click on button called 'Popup Windows'
    page.locator("#PopUp").click() # after click, two pop-ups are displayed

    page.wait_for_timeout(5000)

    all_popups=context.pages
    print("Total number of popups/pages:",len(all_popups))

    # capture urls of all the popup pages
    for pop in all_popups:
        print("Popup/Page URL======>", pop.url)
        title = pop.title()
        if "Playwright" in title:
            # click on button 'Get Started'
            pop.locator(".getStarted_Sjon").click()
            pop.wait_for_timeout(3000)
            expect(pop).to_have_title("Installation | Playwright")
            pop.close()  # close the playwright popup/window

    page.wait_for_timeout(5000)
    context.close()
    browser.close()

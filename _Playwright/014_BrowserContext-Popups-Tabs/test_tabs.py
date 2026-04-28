'''
types of events:

FOR alerts/dialogs -----> USE event:: dialog
FOR download files -----> USE event:: download
FOR popups   -----> USE event:: popup
FOR tabs  ---------> USE event:: page

page.on()
'''

from playwright.sync_api import Playwright

def test_handle_tabs(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    parentpage=context.new_page()

    parentpage.goto("https://testautomationpractice.blogspot.com/")

    # register an event for handle tab, THE EVENT TYPE is called 'page'
    # before clicking to button 'New Tab'
    parentpage.on("page",lambda page:page.wait_for_load_state())

    parentpage.locator("button:has-text('New Tab')").click()
    parentpage.wait_for_timeout(3000)

    all_pages=context.pages
    print("Number of tabs/pages:====>",len(all_pages))

    print("Title of parent page:",all_pages[0].title())
    print("Title of child page/tab:", all_pages[1].title())

    childpage=all_pages[1]
    # to work in the child page use context --> childpage
    print("URL of the child page:=====>",childpage.url)

    context.close()
    browser.close()












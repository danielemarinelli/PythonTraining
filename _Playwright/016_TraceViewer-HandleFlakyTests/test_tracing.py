
from playwright.sync_api import Playwright, sync_playwright, expect

# for tracing feature we need browser and context variable
# all logs , screens, videos will be in the zip file of the trace
def test_traceViewer(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()

    #starting the trace
    context.tracing.start(screenshots=True,snapshots=True)

    page=context.new_page()

    page.goto('https://www.demoblaze.com/index.html')
    page.locator('#login2').click()
    page.locator('#loginusername').fill('pavanol')
    page.locator('#loginpassword').fill('test@123')
    page.locator("button:has-text('Log in')").click()
    page.wait_for_timeout(3000)

    expect(page.locator("#logout2")).to_be_visible()
    expect(page.locator('#nameofuser')).to_contain_text('Welcome pavanol')

    # stopping the trace  and provide the path where store the zip file
    context.tracing.stop(path="trace_the_test.zip")
    #when created, there are two ways to open the .zip file --> cmd line or website
    # cmd ===>> playwright show-trace trace_the_test.zip
    # and a trace viewer window will open!! (time travel feature is present)
    # the website wher edrag&drop the trace.zip file is:
    # =====> https://trace.playwright.dev/
    context.close()
    browser.close()



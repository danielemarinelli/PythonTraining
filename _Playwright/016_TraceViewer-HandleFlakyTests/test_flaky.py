from playwright.sync_api import Page, expect

#want to fail the test intentionally on run time, so we can see the
# re-run feature!
'''
You can retry failed tests automatically in pytest using the pytest-rerunfailures plugin.
1. Install Plugin
pip install pytest-rerunfailures
2. Use CLI command:
pytest _Playwright/016_TraceViewer-HandleFlakyTests/test_flaky.py --headed --reruns 3 --reruns-delay 2
→ This retries failed tests up to 3 times with a 2-second delay between each retry
'''

def test_Login(page: Page):
    page.goto('https://www.demoblaze.com/index.html')
    page.wait_for_timeout(5000)  # user must click on 'Contact' button before script inserts the credentials... test will fail!
    page.locator('#login2').click()
    page.locator('#loginusername').fill('pavanol')
    page.locator('#loginpassword').fill('test@123')
    page.locator("button:has-text('Log in')").click()
    page.wait_for_timeout(5000)
    expect(page.locator("#logout2")).to_be_visible()
    expect(page.locator('#nameofuser')).to_contain_text('Welcome pavanol')
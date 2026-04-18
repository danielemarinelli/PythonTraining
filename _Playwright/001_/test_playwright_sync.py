'''
user guide ---->  https://playwright.dev/python/docs/intro
(PRE-REQUISITE):
Python and Pytest are installed

Install playwright and the browsers with the following 2 commands:

pip install pytest-playwright
playwright install
'''

#playwright has a build-in fixture named --> page and expect
# page is part of Class Page that must be imported from
# module playwright.sync_api
# we need 'expect' build-in fixture to perform assertions
# by default playwright runs in HEADLESS mode (we won't see the UI actions when execution is going)

# Playwright python follows both sync VS async nature. We prefer sync nature where
# the task of the following command starts only when the previous task is over
# Playwright JS or TS are only async nature , so 'await' keyword in front every command

# command to execute ---->
# pytest _Playwright/test_playwright_sync.py -v -s --headed
# pytest _Playwright/test_playwright_sync.py -v -s
# pytest _Playwright/test_playwright_sync.py -v -s --headed --browser chromium --browser firefox
# IN PARALLEL EXECUTION --> pytest test_playwright.py -s -v --headed --browser chromium -n=2

from playwright.sync_api import Page, expect

def test_verifyPageUrl(page:Page):
    page.goto("https://ticket247.co.uk/")  # passing url

    myurl=page.url
    print("Url of the application:", myurl)

    expect(page).to_have_url("https://ticket247.co.uk/") # expected url


def test_verifyTitle(page:Page):
    page.goto("https://ticket247.co.uk/")

    mytitle=page.title()
    print("Title of the page:", mytitle)

    expect(page).to_have_title("Ticket247 | Search, browse and discover live events, gigs and attractions near you")


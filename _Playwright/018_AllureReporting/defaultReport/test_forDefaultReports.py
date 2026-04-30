from playwright.sync_api import Page, expect

# configure config.ini to add basic report
'''
Pytest-html reports
---------
Step 1: Install the plugin
	pip install pytest-html

Step 2: Configure pytest.ini
[pytest]
addopts = --html=myreport.html --self-contained-html --capture=tee-sys

Step 3: Create Sample Tests

Step 4: Run the Tests and Generate Report

Step 5: Attach Screenshots on Test Failures (conftest.py)  - additional step
'''


def test_url(page: Page):
    page.goto('https://www.demoblaze.com/index.html')
    expect(page).to_have_url("https://www.demoblaze.com/index.html")


def test_Title(page: Page):
    page.goto('https://www.demoblaze.com/index.html')
    expect(page).to_have_title("STORE")


def test_google_search(page):
    page.goto("https://www.google.com")
    expect(page).to_have_title("Google")


def test_bing_search(page):
    page.goto("https://www.bing.com/")
    expect(page).to_have_title("Bing123") #Intensionally failed

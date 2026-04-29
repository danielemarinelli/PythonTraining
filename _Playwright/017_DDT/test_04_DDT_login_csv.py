
import pytest
from playwright.sync_api import expect,Page
import csv
from pathlib import Path

login_data=[]    # empty list
user_home = Path.home()  # Get user home directory
csv_file_path = user_home / "PycharmProjects" / "PythonSelenium" / "_Playwright" / "017_DDT" / "testdata" / "data.csv"
file=open(csv_file_path,"r")
# read csv file where data is separated by commas
csvfile=open(csv_file_path, newline='', encoding='utf-8')
reader=csv.DictReader(csvfile)

for row in reader:
    login_data.append((row["email_user"],row["password"],row["validity_credentials"]))


@pytest.mark.parametrize("email, password, validity", login_data)
def test_login_data_driven_csv(email,password,validity,page:Page):
    page.goto("https://demowebshop.tricentis.com/login")

    #fill teh login form
    page.locator("#Email").fill(email)   # email id
    page.locator("#Password").fill(password)  #password
    page.locator("input[value='Log in']").click()

    #validation
    if validity=="valid":
        logout_link=page.locator("a[href='/logout']")
        expect(logout_link).to_be_visible(timeout=5000)
    else:
        error_message=page.locator(".validation-summary-errors")
        expect(error_message).to_be_visible(timeout=5000) # checking error message
        expect(page).to_have_url("https://demowebshop.tricentis.com/login") # checking same login page









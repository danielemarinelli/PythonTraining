
import pytest
from playwright.sync_api import expect,Page
import json
from pathlib import Path

login_data=[]    # empty list

# Read json file
user_home = Path.home()  # Get user home directory
json_file_path = user_home / "PycharmProjects" / "PythonSelenium" / "_Playwright" / "017_DDT" / "testdata" / "data.json"
file=open(json_file_path,"r")
json_data=json.load(file)  # store the data from JSON file to a variable (contains all teh dataset of the json file)

for data in json_data:
    login_data.append((data["email_user"],data["password"],data["validity_credentials"]))  #must match with the KEY on the JSON file


@pytest.mark.parametrize("email, password, validity", login_data)  # "email, password, validity" are user defined and can be anything
def test_login_data_driven_json(email,password,validity,page:Page):
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









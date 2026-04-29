import pytest
from playwright.sync_api import expect,Page

''' combination to test:::
valid credentials -> login successful => TEST PASSED
valid credentials -> login not successful => TEST FAILED
invalid credentials -> login successful => TEST FAILED
invalid credentials -> login not successful => TEST PASSED
'''

# Test data
login_test_data = [
    ("dango@accenture.com", "testing000", "valid"),
    ("invaliduser@example.com", "test321", "invalid"),
    ("validuser@example.com", "testxyz", "invalid"),
    ("", "", "invalid")
]

@pytest.mark.parametrize("email, password, validity", login_test_data)
def test_login_data_driven(email, password, validity, page:Page):

        page.goto("https://demowebshop.tricentis.com/login")

        # Fill login form
        page.locator("#Email").fill(email)
        page.locator("#Password").fill(password)
        page.locator('input[value="Log in"]').click()

        if validity.lower() == "valid":  # valid credentials
            # Assert logout link visible (successful login)
            logout_link = page.locator('a[href="/logout"]')
            expect(logout_link).to_be_visible(timeout=5000)  #logout link is visible
        else:
            # Assert error message is visible (invalid login)
            error_message = page.locator(".validation-summary-errors")
            expect(error_message).to_be_visible(timeout=5000)
            msg= error_message.inner_text()
            print(msg)
            # Assert user remains on login page
            expect(page).to_have_url("https://demowebshop.tricentis.com/login")

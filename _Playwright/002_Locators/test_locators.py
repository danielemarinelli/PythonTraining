# EXECUTE ALL TESTS IN SERIAL: pytest _Playwright/002_Locators/test_locators.py -v -s --headed
# EXECUTE ALL TESTS IN PARALLEL: pytest _Playwright/002_Locators/test_locators.py -v -s --headed -n 2
# EXECUTE ONLY ONE TEST: pytest _Playwright/002_Locators/test_locators.py::test_verify_login_webSite_orange -v -s --headed
# BUILD-IN LOCATORS IN PLAYWRIGHT:
# guide --> https://playwright.dev/python/docs/locators
# 1) page.get_by_alt_text() --> Locate images by their alt attribute
# 2) page.get_by_text() --> Locate by visible text content
# 3) page.get_by_label() --> Locate form controls using associated label text
# 4) page.get_by_role() --> Locate elements by accessibility roles like button, checkbox,
# heading, etc.
# 5) page.get_by_placeholder() --> Locate inputs via placeholder text
# 6) page.get_by_title() --> Locate elements by their title attribute
# 7) page.get_by_test_id() --> Locate by custom attribute like data-testid


import re
from playwright.sync_api import Page, expect

def test_verify_playwrightLocators(page: Page):
    page.goto("https://demo.nopcommerce.com/")
    page.wait_for_timeout(1000)
    # 1)
    logo=page.get_by_alt_text("nopCommerce demo store")  # inspecting the logo , img has the alt text , so we can use the  get_by_alt_text()
    expect(logo).to_be_visible()
    #2)
    expect(page.get_by_text("Featured products")).to_be_visible()
    expect(page.get_by_text("Welcome to our store")).to_be_visible()
    expect(page.get_by_text(re.compile(".*Welcome to.*"))).to_be_visible()  #even partial text is ok, but import module named 're'

def test_verify_pwRoleLocator(page: Page):
    #4) every element has a ROLE, let's locate REGISTER and YOUR PERSONAL DETAILS
    # the 2 elements have h1 and h2 tags and the role is --> HEADING
    # need to pass ROLE and NAME OF ELEMENT:
    page.goto("https://demo.nopcommerce.com/register")
    expect(page.get_by_role("heading", name="Register")).to_be_visible()
    expect(page.get_by_role("heading",name="Your Personal Details")).to_be_visible()


def test_verify_pwLocators_practice(page: Page):
    # 3)
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    page.get_by_label("email").fill("QA.ItalianTeam@gmail.com")
    #page.get_by_label("age-label").fill("99")
    page.wait_for_timeout(1000)
    page.goto("https://demo.nopcommerce.com/register")
    page.get_by_label("First name:").fill("Roy")
    page.get_by_label("Last name:").fill("Allen")
    page.get_by_label("Email:").fill("roy.allen@gmail.com")
    page.wait_for_timeout(1000)

def test_verify_pwLocators_placeHolder(page: Page):
    # 5)
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    page.get_by_placeholder("Enter your full name").fill("Gigi Marino")
    page.get_by_placeholder("Phone number (xxx-xxx-xxxx)").fill("0123456789")
    page.get_by_placeholder("Type your message here...").fill("Learning Python with Playwright")
    page.wait_for_timeout(1000)


def test_verify_pwLocators_getByTitle_getByTestId(page: Page):
    # 6)
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    expect(page.get_by_title("Home page link")).to_have_text("Home")
    expect(page.get_by_title("HyperText Markup Language")).to_have_text("HTML")
    expect(page.get_by_title("Tooltip text")).to_have_text("This text has a tooltip")
    # 7)
    expect(page.get_by_test_id("profile-name")).to_have_text("John Doe")
    expect(page.get_by_test_id("profile-email")).to_have_text("john.doe@example.com")


def test_verify_login_webSite_orange(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button",name=" Login ").click()
    page.wait_for_timeout(1000)
    expect(page.get_by_role("heading",name="Dashboard")).to_be_visible()





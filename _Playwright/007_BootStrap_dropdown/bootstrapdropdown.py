# bootstrap ---> the dropDown options are not visible in the DOM
''' must freeze the page for some time to collect the dropdown options
    one option is freezing with SELECTOR HUB
    Press F12 to inspect page, click setting icon
    in the left side click on 'Ignore list' and
    uncheck the option ---> 'Enable ignore listing'
    close setting and
    click on the UI button to open the DropDown list
    and go to SELECTORHUB:
    click on the 4th icon (Turn on debugger), now we can capture the DOM and xpath for the options
'''
from playwright.sync_api import sync_playwright, expect, Page


def test_bootstrapdropdown(page : Page):
    # Launch the URL
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Login steps
    page.locator('[name="username"]').fill('Admin')
    page.locator('[name="password"]').fill('admin123')
    page.locator('[type="submit"]').click()

    page.wait_for_timeout(5000)

    # click on PIM
    page.get_by_text('PIM').click()

    page.wait_for_timeout(2000)
    # click on the Job title dropdown
    page.locator("form i").nth(2).click()  # this will open options from the dropdown
    page.wait_for_timeout(3000)

    # capture all the options from dropdown
    options = page.locator("//div[@role='listbox']//span")
    page.wait_for_timeout(3000)
    count = options.count()  # get the count of options
    print("Number of options in the dropdown:", count)

    expect(options).to_have_count(count) # assertion for counting the options

    page.wait_for_timeout(2000)
    # Print all the options from dropdown
    print("All the options from the dropdown in list format===>", options.all_text_contents())

    # Print all the options text using loop
    for i in range(count):
        print(options.nth(i).text_content())

        # select/click on specific option
        for i in range(count):
            text = options.nth(i).inner_text()
            if text == 'Automation Tester':
                print("Matching success.....")
                options.nth(i).click()
                break

        page.wait_for_timeout(5000)



from playwright.sync_api import Page, expect


def test_insert_singleDropDowns(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # 3 ways to select option from the dropdown
    #1)
    page.locator("#country").select_option("United Kingdom")  # by label
    #page.locator("#country").select_option(label="United Kingdom")  # by label

    selected_value = page.locator("#country").input_value()  # capture selected option
    print("Selected Value:", selected_value)
    # 2)
    page.locator("#country").select_option("japan")  #by value (value is in the DOM)
    # page.locator("#country").select_option(value="japan")  # by value
    # 3)
    page.wait_for_timeout(2000)
    page.locator("#country").select_option(index=3)   # by index  # index starts from 0
    page.wait_for_timeout(2000)
    # check number of options in dropdown
'''
    dropdown_options = page.locator("#country>option")
    expect(dropdown_options).to_have_count(10)

    options_text = [text.strip() for text in dropdown_options.all_text_contents()]
    print(options_text)

    # print countries using loop
    for option in options_text:
        print(option)

    page.wait_for_timeout(2000)'''







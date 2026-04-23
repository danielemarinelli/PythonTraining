import pytest
from playwright.sync_api import Page, expect


def test_jquery_datepicker(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # working on Date Picker 1 on the UI:

    date_input = page.locator("#datepicker")

    # Approach 1:
    # date_input.fill("10/15/2025")   # mm/dd/yyyy

    # Approach 2: select the date , it can be even in the past
    is_future = False
    year = "2024"
    month = "October"
    date = "15"

    date_input.click()  # opens datepicker
    select_date(page, year, month, date, is_future)
    print("Selected date====>:", date_input.input_value())
    expect(date_input).to_have_value("10/15/2024")

    page.wait_for_timeout(5000)


def select_date(page, taget_year, target_month, target_date, is_future):
    # while loop selects month and year from the  date picker
    while True:
        current_month = page.locator('.ui-datepicker-month').text_content()
        current_year = page.locator('.ui-datepicker-year').text_content()

        if current_month == target_month and current_year == taget_year:
            break  # this means that we are in the correct month and year
        # another if block to understand if click on past ot future arrow:
        if is_future == True:
            page.locator(".ui-datepicker-next").click()  # click for future dates
        else:
            page.locator(".ui-datepicker-prev").click()  # click for past dates

    all_dates = page.locator(
        ".ui-datepicker-calendar td").all()  # capture all dates from datepicker and convert it in list

    # selecting date from the date picker.
    for dt in all_dates:
        date_text = dt.inner_text()
        if (date_text == target_date):
            dt.click()  # we found the target date so we can break the loop
            break



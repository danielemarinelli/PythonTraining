import pytest

from playwright.sync_api import expect

# Test data to insert in field to search a product in the web page is in a LIST
search_items = ['laptop', 'Gift card', 'smartphone', 'monitor']
# the test will run for 4 times, based on the items in the list:
# 'monitor' is not present in the web page, so one test will fail

# use decorator from pytest called: --> parametrize
@pytest.mark.parametrize("item", search_items)
def test_search_items(item, page):
    page.goto("https://demowebshop.tricentis.com/")

    # Fill search box and click search button
    page.locator("#small-searchterms").fill(item)
    page.locator("input[value='Search']").click()

    # Assertion: first result title should contain the search item
    first_result = page.locator("h2 a").nth(0)  # get the first product
    expect(first_result).to_contain_text(item, ignore_case=True) #parameter the ignore the upper and lower letters

''' DOM                css to locate web element (tags are optional)
MOST COMMON CSS LOCATORS
tag id          ----> tag#id
tag class       ----> tag.class
tag attribute   ----> tag[attribute=value]
tag class attribute   ----> tag.class[attribute=value]

'''

import pytest
from playwright.sync_api import Page, expect

def test_verify_css_loc(page: Page):
    page.goto("https://demowebshop.tricentis.com")

    # tag id , both ways are ok, tag=input is optional
    # insert a product ('phone') in search field
    page.locator("input#small-searchterms").fill("phone")
    page.locator("#small-searchterms").fill("phone")
    page.wait_for_timeout(1000)

    # tag class , both ways are ok, tag=input is optional
    #tag class
    # the ---> class=search-box-text ui-autocomplete-input , NB: ignore the part after the space!!!
    page.locator("input.search-box-text").clear()
    page.locator(".search-box-text").fill("t-shirt")
    page.wait_for_timeout(2000)

    # tag attribute , both ways are ok, tag=input is optional
    # from DOME , attribute value=Search store  , NB: Must be inserted in single ' ' because there is a space between two words
    page.locator("input[value='Search store']").clear()
    page.locator("input[value='Search store']").fill("computer")
    page.wait_for_timeout(2000)

    # tag class attribute --> tag.class[attribute=value]
    page.locator("input.search-box-text[name=q]").clear()
    page.locator(".search-box-text[name=q]").fill("phone")
    page.wait_for_timeout(2000)





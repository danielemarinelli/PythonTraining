'''
relative xpath --> tag[@attribute='value']
'''

import pytest
from playwright.sync_api import Page, expect

def test_verify_xpath_loc(page: Page):
    page.goto("https://demo.nopcommerce.com/")
    # relative xpath
    page.locator("(//a[@href='/digital-downloads'])[1]").click()
    page.wait_for_timeout(1000)
    # xpath with contains
    expect(page.locator("(//a[contains(@href,'donation')])[2]")).to_be_visible()

    # get me the count of products with 'computer'
    page.goto("https://demowebshop.tricentis.com")
    products = page.locator("//h2/a[contains(@href,'computer')]")
    products_count=products.count()
    print("Computer listed are: ",products_count)
    expect(products).to_have_count(products_count)

    # get text of first , last and middle product name:
    print("1st pc name: ", products.first.text_content())   # text_content() is equal to getText()
    print("last pc name: ", products.last.text_content())
    print("third pc name: ", products.nth(2).text_content())  #nth() index starts from 0

    # if I insert all products titles in list format, then I can do loops with them
    product_title = products.all_text_contents()
    print("Product titles: ", product_title)
    print("Printing titles from looping statement---->")
    for i in product_title:
        print(i)

    # xpath --> start-with() , let's capture products that in the title start with Build
    build_pro = page.locator("//h2/a[starts-with(@href,'/build')]")
    print("Build product are: ",build_pro.count())
    expect(build_pro).to_have_count(build_pro.count())

    # xpath --> text()
    page.locator("//span[text()='Shopping cart']").click()
    msg = page.locator("//div[@class='order-summary-content']").text_content()
    print(msg.strip())   # strip() cancel all blank spaces in string

    # xpath  --> last() at bottom page there are links,
    # let's print the last link under section 'FOLLOW US'
    google_link=page.locator("//div[@class='column follow-us']//li[last()]")
    print(google_link.text_content())
    expect(google_link).to_be_visible()
    # can even insert index instead of last():
    youtube_link = page.locator("//div[@class='column follow-us']//li[4]")
    expect(youtube_link).to_be_visible()
    google_link.click()

    # xpath  --> position()
    tw_link = page.locator("//div[@class='column follow-us']//li[position()=2]")
    expect(tw_link).to_have_text("Twitter")

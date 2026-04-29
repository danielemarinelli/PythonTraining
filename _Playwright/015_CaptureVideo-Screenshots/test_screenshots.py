from playwright.sync_api import sync_playwright, expect, Page
import time
import datetime

# different ways to capture the screenshot , no need to create context and browser

def test_screenshots_ways(page:Page):
    page.goto("https://demowebshop.tricentis.com/")

    #currect time stamp , two ways: with time() method casting to string
    #timestamp=str(int(time.time()))
    #time in different formats
    timestamp=datetime.datetime.now().strftime("%Y%m%d%H%M%S")


    # Page screenshot (partially visible)
    #page.screenshot(path=f"screenshots/homepage_{timestamp}.png") # path where we want to store the screenshot

    # Full page screenshot
    page.screenshot(path=f"screenshots/homepage_{timestamp}.png", full_page=True)


    # Element/specific section of the page screenshot
    logo=page.locator("img[alt='Tricentis Demo Web Shop']")
    logo.screenshot(path=f"screenshots/logo_{timestamp}.png")

    # specific section
    featured_products=page.locator(".product-grid.home-page-product-grid")
    featured_products.screenshot(path=f"screenshots/featured_Products_{timestamp}.png")



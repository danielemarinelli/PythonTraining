from playwright.async_api import Page
from playwright.sync_api import sync_playwright, expect


def test_comparison_of_methods(page: Page):
    page.goto("https://demowebshop.tricentis.com/")

    products = page.locator(".product-title")  # 6 products

    # 1) inner_text() vs text_content()

    print("Using inner_text() -EXACT TEXT-====> ",products.nth(1).inner_text()) # return actual text
    print("Using text_content() -TEXT WITH SPACES-====> ",products.nth(1).text_content()) # returns content with special chars and spaces
    print('------<<<<<zzzzzzz---------->>>>>>>>>>')
    count=products.count()
    for i in range(count):
        product_name=products.nth(i).text_content()
        print(product_name)
        #print(product_name.strip())

    print("Using inner_text() -better-====> ")
    for i in range(count):
        product_name = products.nth(i).inner_text()  # inner_text doesn't need strip
        print(product_name)

    # 2) all_inner_texts() vs all_text_contents()  --- both return LIST of Collection
    print("all_inner_texts() vs all_text_contents()====> ")
    product_names_all_inner = products.all_inner_texts()
    product_names_all_contents = products.all_text_contents()
    print(product_names_all_inner)
    print("all_contents before trimming",product_names_all_contents)
    products_names_trimmed=[text.strip() for text in product_names_all_contents]
    print("all_contents after trimming is same of all_inner",products_names_trimmed)

    # 3) all()
    product_locators = products.all()   # all() returns a list of locators
    print("first product:",product_locators[0].inner_text())

    # two ways to print the products text displayed
    for product_loc in product_locators:
        print(product_loc.inner_text())

    for i in range(len(product_locators)):
        print(product_locators[i].inner_text())








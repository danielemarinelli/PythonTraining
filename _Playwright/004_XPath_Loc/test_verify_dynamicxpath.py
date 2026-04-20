'''
THERE IS A DYNAMIC BUTTON -START/STOP- and xpath changes
All these xpaths below can locate the button that changes dynamically
//button[@name='start' or @name='stop'] or
//button[contains(@name,'st')] contains()
//button[starts-with(@name,'st')] starts-with()
//button[text()='STOP' or text()='START']; text() - innertext

even CSS
button[name='start'],button[name='stop']   # with tags
[name='start'],[name='stop']    # without tags
button[name^='st']    #  -->   ^ means 'starts with' , equals to start-with() in xpath
button[name*='st']    #  -->   * means 'contains' ,  equals to contains() in xpath
'''


from playwright.sync_api import Page, expect

def test_verify_dynamicxpath(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    for i in range(5):  # clicking 5 times on the button
        # with xpath
        page.locator("//button[@name='start' or @name='stop']").click()
        page.wait_for_timeout(1000)

    for i in range(5):  # clicking 5 times on the button
        # with CSS
        page.locator("[name='start'],[name='stop']").click()
        page.wait_for_timeout(1000)


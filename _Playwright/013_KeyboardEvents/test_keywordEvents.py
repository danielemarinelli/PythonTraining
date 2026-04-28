from playwright.sync_api import sync_playwright, expect, Page

def test_keyboard_actions(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    input1=page.locator("#input1")   # copy and paste string with ctrlc ctrlv in Sections 1 - 2 - 3
    # keyboard is the WORD to use:
    #1. focus on input1   method focus()
    input1.focus()

    #2. provide the text in input1   - another method beside fill()
    page.keyboard.insert_text("welcome in Italy!!")

    #3 . ctrl + A
    page.keyboard.press("Control+A")

    #4 ctrl + C
    page.keyboard.press("Control+C")   # copy the string!

    # 5. press Tab key twice to navigate/focus on input2
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")

    #6. Ctrl +V  - Paste the text inside the 2nd inputbox - input2
    page.keyboard.press("Control+V")

    # 7. press Tab key twice to navigate/focus on input3
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")

    # 8. Ctrl +V  - Paste the text inside the 3nd inputbox - input3
    page.keyboard.press("Control+V")

    # validate the texts inside the fields
    input2=page.locator("#input2")
    input3=page.locator("#input3")

    expect(input2).to_have_value("welcome in Italy!!")
    expect(input3).to_have_value("welcome in Italy!!")

    page.wait_for_timeout(5000)
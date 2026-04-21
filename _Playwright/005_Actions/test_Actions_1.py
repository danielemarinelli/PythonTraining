
from playwright.sync_api import Page, expect

def test_insert_inputBox(page: Page):
    page.goto("https://practice-automation.com/form-fields/")
    expect(page.locator("#name-input")).to_be_visible()
    expect(page.locator("//input[@type='password']")).to_be_visible()
    page.locator("#name-input").fill("daniele_QAteam")
    page.locator("//input[@type='password']").fill("01234")

    page.wait_for_timeout(2000)


def test_check_radioBtn(page: Page):
    page.goto("https://practice-automation.com/form-fields/")
    radio_btns = page.locator("//input[@type='radio']")  # return locators
    print(radio_btns)
    print(radio_btns.count())
    colors = ['Red', 'Green', 'Yellow', 'Blue', '#FFC0CB' ]
    colors_radio = []
    for color in colors:
        radio = page.get_by_label(color)
        colors_radio.append(radio)
    print("total number of radio buttons:", len(colors_radio))
    print(colors_radio)
    page.get_by_label("Yellow").check()
    page.wait_for_timeout(2000)

    radio_list=radio_btns.all()    # converting locators radio_btns in a list
    print("Ecco il terzo radio button: ",radio_list[2].inner_text())


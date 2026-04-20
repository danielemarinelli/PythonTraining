
from playwright.sync_api import Page, expect

def test_verify_inputBox(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    email_text_box = page.locator("#email")
    # visibility of element and enable
    expect(email_text_box).to_be_visible()
    expect(email_text_box).to_be_enabled()

    # check the attribute of the elements (from the DOM)
    expect(email_text_box).to_have_attribute("maxlength", "25")
    expect(email_text_box).to_have_attribute("placeholder", "Enter EMail")
    # get an attribute of the element
    maxlength = email_text_box.get_attribute("maxlength")
    placeholder_email = email_text_box.get_attribute("placeholder")
    print("Maximum length of inputbox:", maxlength)
    print("Email placeholder:", placeholder_email)

    # Fill the text
    email_text_box.fill("qateam@qa.com")

    # check the input value inserted from fill() in inputbox
    enteredvalue = email_text_box.input_value()
    print("User entered this email:", enteredvalue)

    page.wait_for_timeout(1000)


def test_verify_radioButton(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    # Radio button ---> only one choice can be picked
    male_radio = page.locator("#male")
    female_radio = page.locator("#female")
    # visibility of the element and enable or not
    expect(male_radio).to_be_visible()
    expect(male_radio).to_be_enabled()
    expect(female_radio).to_be_visible()
    expect(female_radio).to_be_enabled()

    # Male radio button should not be checked (default)
    expect(male_radio).not_to_be_checked()
    expect(female_radio).not_to_be_checked()

    # Select/Check radio button - action
    male_radio.check()

    # Male radio button should not be checked ( default)
    expect(male_radio).to_be_checked()

    female_radio.check()
    expect(female_radio).to_be_checked()
    page.wait_for_timeout(1000)


def test_verify_checkBox(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    # CheckBox  ---> multiple choice can be picked

    # 1. select specific checkbox (Sunday)
    #sunday_checkbox = page.get_by_label("Sunday")
    #sunday_checkbox.check()
    #expect(sunday_checkbox).to_be_checked()

    # 2. count number of check boxes

    # step1: all labels in a list
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    checkboxes = []

    # step2
    for day in days:
        checkbox = page.get_by_label(day)
        checkboxes.append(checkbox)
    # for loop in one single line:
    #checkboxes = [page.get_by_label(day) for day in days]
    print("total number of checkboxes:", len(checkboxes))

    # 3 . select all the checkboxes and assert each check box is selected
    for checkbox in checkboxes:
        checkbox.check()
        expect(checkbox).to_be_checked()

    page.wait_for_timeout(2000)

    # 4. check last 3 checkboxes
    for checkbox in checkboxes[-3:]:
        checkbox.uncheck()
        expect(checkbox).not_to_be_checked()

    page.wait_for_timeout(2000)

    # 5. Toggle checkboxes.

    for checkbox in checkboxes:
        if checkbox.is_checked():
            checkbox.uncheck()
            expect(checkbox).not_to_be_checked()
        else:
            checkbox.check()
            expect(checkbox).to_be_checked()

    page.wait_for_timeout(2000)

    # 6. Randomly check checkboxes - check 1,3 6 checkboxes
    indexes = [1, 3, 6]

    for i in indexes:
        checkboxes[i].check()
        expect(checkboxes[i]).to_be_checked()

    page.wait_for_timeout(2000)

    # 7. select checkbox based on the label/input value by choice
    weekday = "Friday"

    for label in days:
        if label == weekday:
            checkbox = page.get_by_label(label)
            checkbox.check()
            expect(checkbox).to_be_checked()

    page.wait_for_timeout(3000)




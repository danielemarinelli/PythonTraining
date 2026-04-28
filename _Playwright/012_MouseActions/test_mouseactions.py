import pytest
from playwright.sync_api import sync_playwright, expect,Page

@pytest.mark.skip
def test_mouse_hover(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    point_me=page.locator(".dropbtn") #mouse hover on POINT ME button
    point_me.hover()  # when hovering, two elements are displayed

    laptops=page.locator('.dropdown-content a:nth-child(2)')  #CSS nth-child index starts from 1
          #page.locator('.dropdown-content a').nth(0)  with method .nth() indexes start from 0
    laptops.hover()    # picking laptops option

    page.wait_for_timeout(2000)

@pytest.mark.skip
def test_mouse_rightclick(page:Page):
    page.goto("http://swisnl.github.io/jQuery-contextMenu/demo.html")

    button=page.locator(".context-menu-one")
    button.click(button="right") # performs right click action - right , left, middle

    page.wait_for_timeout(3000)


def test_mouse_doubleclick(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    filed1 = page.locator("#field1")
    filed1.clear()
    filed1.fill("Go Italy!!")

    btncopy=page.locator("button[ondblclick='myFunction1()']")
    btncopy.dblclick()  # performs double click action on BUTTON -> COPY TEXT

    filed2=page.locator("#field2")
    expect(filed2).to_have_value("Go Italy!!")

    page.wait_for_timeout(5000)


def test_mouse_draganddrop(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    source=page.locator("#draggable")
    target=page.locator("droppable")

    #Approach1 : manual drag using hover()
    # source.hover()
    # page.mouse.down()
    # target.hover()
    # page.mouse.up()

    #Approach 2 : drag_to()   one statement!!
    source.drag_to(target)

    page.wait_for_timeout(5000)

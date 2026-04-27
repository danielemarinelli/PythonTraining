import pytest
from playwright.sync_api import sync_playwright, expect,Page


def test_nested_frames(page: Page):
    page.goto("https://ui.vision/demo/webtest/frames/")

    # frame 3
    #frame3=page.frame_locator("frame[src='frame_3.html']") # grab frame 3 with CSS or below with URL
    frame3 = page.frame(url="https://ui.vision/demo/webtest/frames/frame_3.html")  # grab frame 3

    frame3.locator("input[name='mytext3']").fill("Welcome") # get the inputbox from frame 3 and provide the text

    child_frames=frame3.child_frames  # method to count the nested frames inside the main frame, RETURNS A LIST OF FRAMES
    print("Number of child frames inside frame 3: ", len(child_frames))

    innerframe=child_frames[0]  # this is the nested frame and we can iterate with the elements inside

    radio=innerframe.get_by_label("I am a human")  #radiobutton
    radio.check()
    expect(radio).to_be_checked()


    page.wait_for_timeout(3000)
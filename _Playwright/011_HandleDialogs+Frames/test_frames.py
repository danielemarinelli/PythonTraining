import pytest
from playwright.sync_api import sync_playwright, expect,Page


def test_frames(page: Page):
    page.goto("https://ui.vision/demo/webtest/frames/")

    frames=page.frames    # this method gives up back the number of frames
    print("Number of frames on a page:", len(frames))  # 7

    # option 1 to get a frame:
    # for frames, we use frame_locator method, this gets the frame

    frame1 = page.frame_locator("frame[src='frame_1.html']")
    frame1.locator("input[name='mytext1']").fill("Italy")  # we use frame1.locator with CSS instead of page.locator as usual

    page.wait_for_timeout(2000)

    # option 2 to get a frame:
    # using URL from the DOM of html
    frame1 = page.frame(url='https://ui.vision/demo/webtest/frames/frame_1.html')  # option 2: get the frame using url
    inputbox = frame1.locator("input[name='mytext1']")
    inputbox.fill("Going for option2...")

    expect(inputbox).to_have_value("Going for option2...")

    page.wait_for_timeout(2000)

    #option 3 is get the frame by name is there is name= in DOM as attribute
    # frame1=page.frame("name of the frame in DOM")  # options 3: get the frame using name  ( We cannot use here since we do not have name for the frame 1


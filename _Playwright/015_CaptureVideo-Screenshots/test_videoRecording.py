
from playwright.sync_api import Playwright, sync_playwright, expect
from pathlib import Path

def test_record_video(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    user_home = Path.home()  # Get user home directory
    video_file_path = user_home / "PycharmProjects" / "PythonSelenium" / "_Playwright" / "015_CaptureVideo-Screenshots" / "videos"
    context=browser.new_context(
           record_video_dir=video_file_path,  #the folder where the video will be stored
           record_video_size={"width":1024,"height":768}
    )
    page=context.new_page()

    page.goto('https://www.demoblaze.com/index.html')
    page.locator('#login2').click()
    page.locator('#loginusername').fill('pavanol')
    page.locator('#loginpassword').fill('test@123')
    page.locator("button:has-text('Log in')").click()
    page.wait_for_timeout(3000)

    expect(page.locator("#logout2")).to_be_visible()  # verify log out button is visible
    expect(page.locator('#nameofuser')).to_contain_text('Welcome pavanol')  # verify username displayed

    context.close()   # always to close context and browser
    browser.close()



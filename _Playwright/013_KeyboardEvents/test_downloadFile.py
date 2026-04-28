from playwright.sync_api import sync_playwright, expect, Page
import os
from pathlib import Path

user_home = Path.home()      # Get user home directory
file_path = user_home / "PycharmProjects" / "PythonSelenium" / "_Playwright" / "013_KeyboardEvents" / "downloads" / "weather.txt"

def test_download_file(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/p/download-files_25.html")

    page.locator("#inputText").fill("Today it is a sunny day...")
    page.locator("#generateTxt").click()  # this will generate a link to download the file

    # # Approach 1: to download we need to register an event with def function
    #def handle_download(download):  # the event name is called 'download'
    #    download.save_as(file_path) # saved inside the path framework#
    #page.on("download", handle_download)
    #page.locator("#txtDownloadLink").click()  # this will download the file



    # Approach 2: we can create lambda function:
    page.on("download",lambda download: download.save_as(file_path))

    page.locator("#txtDownloadLink").click()  # this will download the file

    page.wait_for_timeout(3000)

    # validation
    if os.path.exists(file_path):
        print("File exists")
    else:
        print("File not exist")


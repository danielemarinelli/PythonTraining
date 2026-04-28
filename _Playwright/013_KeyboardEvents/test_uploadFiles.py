from playwright.sync_api import expect, Page
import pytest
from pathlib import Path

user_home = Path.home()      # Get user home directory

@pytest.mark.skip
def test_upload_singlefile(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    #uploading single file
    # method --> set_input_files() and specify the path
    file_path = user_home / "PycharmProjects" / "PythonSelenium" / "_Playwright" / "013_KeyboardEvents" / "file" / "Notes.txt"
    page.locator("#singleFileInput").set_input_files(file_path)

    #page.locator("#singleFileInput").set_input_files("_Playwright\\013_KeyboardEvents\\file\\Notes.txt")
    page.locator("button:has-text('Upload Single File')").click()  # CSS

    #validation
    expect(page.locator("#singleFileStatus")).to_contain_text("Notes.txt")
    print("File uplaod ok......")
    page.wait_for_timeout(3000)


def test_upload_multiplefiles(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    #uploading multiple files in a list
    file1_path = user_home / "PycharmProjects" / "PythonSelenium" / "_Playwright" / "013_KeyboardEvents" / "file" / "Notes.txt"
    file2_path = user_home / "PycharmProjects" / "PythonSelenium" / "_Playwright" / "013_KeyboardEvents" / "file" / "NATO.jpg"
    files=[file1_path,file2_path]
    page.locator("#multipleFilesInput").set_input_files(files)
    page.locator("button:has-text('Upload Multiple Files')").click()

    #validation
    msgloc=page.locator("#multipleFilesStatus")

    expect(msgloc).to_contain_text("NATO.jpg")
    expect(msgloc).to_contain_text("Notes.txt")

    page.wait_for_timeout(3000)

    print("Multiple files are uploaded successfully.......")

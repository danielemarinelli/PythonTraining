# Pre-requisite for Asynchronous execution
# install  pytest-asyncio
# command:   pip install pytest-asyncio

# DON'T FOLLOW THIS async APPROACH

from playwright.async_api import async_playwright,Page, expect
import pytest

@pytest.mark.asyncio
async def test_verifyPageUrl_async():
    async with async_playwright() as plw:
        browser = await plw.chromium.launch(headless=False)  #  headed mode
        mypage = await browser.new_page()
        await mypage.goto("https://ticket247.co.uk/")
        await expect(mypage).to_have_url("https://ticket247.co.uk/")
        await browser.close()


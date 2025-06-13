import time
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')  #will run in backend, user won't see anything
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--incognito')  #run in icognito mode
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
print(driver.title)
driver.implicitly_wait(3)
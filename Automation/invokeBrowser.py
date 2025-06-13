import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.python.org")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
time.sleep(2)

driver = webdriver.Firefox()
driver.get("https://www.wizdomqa.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
time.sleep(2)

driver = webdriver.Edge()
driver.get("https://demoqa.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
time.sleep(2)


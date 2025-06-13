import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
time.sleep(1)
driver.find_element(By.XPATH,"//a[text()='Click Here']").click()

allWindowsOpened = driver.window_handles
print(allWindowsOpened)
#child window is stores in the list with index = 1
driver.switch_to.window(driver.window_handles[1])

time.sleep(2)
print(driver.find_element(By.TAG_NAME,"h3").text)
assert driver.find_element(By.TAG_NAME,"h3").text == "New Window"
driver.close() #closing the child window
driver.switch_to.window(driver.window_handles[0])
msg = driver.find_element(By.TAG_NAME,"h3").text
print(msg)
assert msg == "Opening a new window"


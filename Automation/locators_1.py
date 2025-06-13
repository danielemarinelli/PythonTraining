import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
# xpath --> //a[text()='Forgot password?']
time.sleep(2)
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("demo@gmail.com")
time.sleep(2)
driver.find_element(By.XPATH,"//form/div[2]/input").send_keys("<PASSWORD>")
time.sleep(2)
#confirming the password
driver.find_element(By.XPATH,"//input[@id='userPassword']").send_keys("<PASSWORD>")
time.sleep(2)
driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()
print(driver.current_url)
print("Password has changes successfully!!!!")

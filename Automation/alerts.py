import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
time.sleep(2)
name = driver.find_element(By.XPATH,"//input[@id='name']")
name.send_keys("Daniele")
driver.find_element(By.XPATH,"//input[@id='alertbtn']").click()
time.sleep(2)
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
assert "Hello" in alertText
alert.accept()  #positive alert
#alert.dismiss() #not accepting the alert





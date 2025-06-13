import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")
driver.maximize_window()
fruit = "Apple"
driver.implicitly_wait(3)
#PRINT PRICE OF APPLE: but xpath is HARDCODED with Apple and cell-4-undefined
apple_price = driver.find_element(By.XPATH,"//div[text()='Apple']/../../div[@id='cell-4-undefined']")
print(apple_price.text)
#DYNAMIC XPATH , if dev addes columns the 4 of id -> cell-4-undefined must be dynamic:
apple_price_column_from_table = driver.find_element(By.XPATH,"//div[text()='Price']").get_attribute("data-column-id")
print(apple_price_column_from_table)
apple_p = driver.find_element(By.XPATH,"//div[text()='"+fruit+"']/../../div[@id='cell-"+apple_price_column_from_table+"-undefined']").text
print(apple_p)






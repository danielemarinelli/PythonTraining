import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='autosuggest']").send_keys("us")
time.sleep(2)
countries = driver.find_elements(By.XPATH,"//ul[@id='ui-id-1']/li/a")
print(len(countries))
for country in countries:
  print(country.text)
  if country.text == "Mauritius":
      country.click()
      break
time.sleep(1)

assert driver.find_element(By.XPATH,"//input[@id='autosuggest']").get_attribute("value") == "Mauritius"




import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(3)
driver.find_element(By.LINK_TEXT,"Top Deals").click()
time.sleep(1)
#switch to other window
allWindowsOpened = driver.window_handles
#print(allWindowsOpened)
#child window is stores in the list with index = 1
driver.switch_to.window(driver.window_handles[1])
driver.find_element(By.XPATH,"//select[@id='page-menu']").click()
time.sleep(1)
s = Select(driver.find_element(By.XPATH,"//select[@id='page-menu']"))
s.select_by_visible_text("10")
time.sleep(2)
#click on column header to sort the veggies VEGGIELIST (A,B,C) browser sort
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
time.sleep(2)
#collect names in  VEGGIELIST and sort list with python SORTVEGGIELIST
veggies = []
veggies = driver.find_elements(By.XPATH,"//tbody/tr/td[1]")
v = []
for veggy in veggies:
    print(veggy.text)
    v.append(veggy.text)

originalBrowserSortedList = v.copy()

v.sort()
print(v)
print(len(v))
print(originalBrowserSortedList)


#print(veggieList)
# SORTVEGGIELIST == VEGGIELIST to check that the sort is ok and list are equal
assert v == originalBrowserSortedList # if equal the two lists are equal and sort worked!!




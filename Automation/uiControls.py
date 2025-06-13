import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
time.sleep(2)
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(checkboxes))
#GOAL click on option2
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        break
assert checkbox.is_selected()  #assert by default IS TRUE
time.sleep(2)

#GOAL click on Radio3
driver.find_element(By.XPATH,"//input[@value='radio3']").click()
time.sleep(1)
assert driver.find_element(By.XPATH,"//input[@value='radio3']").is_selected()

print("Radio3 button and Option2 are both selected. Test Passed!!")
# example hide / show  element in webpage
assert driver.find_element(By.XPATH,"//input[@id='displayed-text']").is_displayed()
# click on the hide button:
driver.find_element(By.XPATH,"//input[@id='hide-textbox']").click()

assert not driver.find_element(By.XPATH,"//input[@id='displayed-text']").is_displayed()
print("hidden field. Test Passed!!")

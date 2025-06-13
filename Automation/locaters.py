import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
time.sleep(5)
# syntax for CSS Selector ---> tagname[attribute='value_attibute']
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("DanieleM")

# syntax for XPATH --->//tagname[@attribute='value_attibute']
driver.find_element(By.XPATH,"//input[@name='email']").send_keys("daniele@gmail.com")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='exampleInputPassword1']").send_keys("12345678")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='exampleCheck1']").click()
time.sleep(2)
driver.find_element(By.ID,"exampleCheck1").click()
time.sleep(2)
#Dropdown in Python
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
time.sleep(2)
dropdown.select_by_index(0)
time.sleep(2)
#----end Select
driver.find_element(By.XPATH,"//input[@id='inlineRadio1']").click()
time.sleep(2)
driver.find_element(By.XPATH,"(//input[@name='name'])[2]").send_keys("Test in Python...")
driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(2)
msg = driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']").text
msg1 = driver.find_element(By.CLASS_NAME,"alert-success").text
time.sleep(2)
print("-with xpath ", msg)
print("-with classname ",msg1)

assert "Success" in msg

driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()
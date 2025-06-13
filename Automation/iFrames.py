import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
time.sleep(1)

driver.execute_script("window.scrollTo(0,500);")
driver.switch_to.frame("courses-iframe")
driver.find_element(By.LINK_TEXT,"Job Support").click()
time.sleep(1)
driver.find_element(By.XPATH,"//input[@name='username']").send_keys("DANIELEM")
time.sleep(4)
driver.find_element(By.XPATH,"//input[@id='mobileno']").send_keys("892376540")
time.sleep(2)
driver.get_screenshot_as_file("iframe_screen.jpg")



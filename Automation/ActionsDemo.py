import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
time.sleep(1)
action = ActionChains(driver)
#action.double_click()
#action.context_click()
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
#right click on TOP menu
time.sleep(3)
action.context_click(driver.find_element(By.XPATH,"(//div[@class='mouse-hover']/div/a)[1]")).perform()
time.sleep(3)




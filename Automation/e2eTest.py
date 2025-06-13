import time

import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice")
driver.maximize_window()
driver.implicitly_wait(5)
#click on SHOP button
driver.find_element(By.XPATH,"//a[text()='Shop']").click()

#select the blackberry that could change position in the webpage
products = driver.find_elements(By.XPATH,"//div[@class='card h-100']")
which_product = "Blackberry"
print(len(products))

for product in products:  #(CHAINING OF WEBELEMENT:)
    productName = product.find_element(By.XPATH,"div/h4/a").text
    if productName == which_product:
        #click ADD TO CART button (CHAINING OF WEBELEMENT:)
        product.find_element(By.XPATH, "div/button").click()
    #print(product.text)
    print(productName)
#click on the red checkout button
driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click()
time.sleep(2)
#click on the green checkout button
driver.find_element(By.XPATH,"(//button[@type='button'])[4]").click()

driver.find_element(By.XPATH,"//input[@id='country']").send_keys("us")

wait_countries = WebDriverWait(driver, 10)
wait_countries.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"Belarus")))

driver.find_element(By.LINK_TEXT,"Belarus").click()

driver.find_element(By.XPATH,"//label[@for='checkbox2']").click()
#click on submit button
driver.find_element(By.XPATH,"//input[@type='submit']").click()

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@class='alert alert-success alert-dismissible']")))

succ_msg = driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']").text
#succ_msg_disp = succ_msg.strip()

assert "Success! Thank you!" in succ_msg

driver.close()






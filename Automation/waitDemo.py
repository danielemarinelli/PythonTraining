import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(3)
driver.find_element(By.XPATH,"//input[@type='search']").send_keys("ber")
time.sleep(2)
tot_products = driver.find_elements(By.XPATH,"//div[@class='products']/div")
print(len(tot_products))
assert len(tot_products) > 0
list_products = []
name_products = driver.find_elements(By.XPATH,"//h4[@class='product-name']")
for product in tot_products: #chaining the webelements parent-child
    product.find_element(By.XPATH,"//button[text()='ADD TO CART']").click()
time.sleep(1)

for name in name_products:
    list_products.append(name.text)
print(list_products)
#click to cart in the top right corner
driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH,"//button[@class='promoBtn']").click()

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//span[@class='promoInfo']")))
print(driver.find_element(By.XPATH,"//span[@class='promoInfo']").text)

#check total amount of products (SUM VALIDATION)
prices = driver.find_elements(By.XPATH,"//tbody/tr/td[5]/p")
sum = 0
for price in prices:
    sum += int(price.text)
print(sum)

tot_amount_displayed = driver.find_element(By.XPATH,"//span[@class='totAmt']").text
assert int(tot_amount_displayed) == sum

discount_amount_displayed = driver.find_element(By.XPATH,"//span[@class='discountAmt']").text
assert int(float(discount_amount_displayed)) < sum

list_selected_products = driver.find_elements(By.XPATH,"//tbody/tr/td[2]/p")
list_ps = []
for product in list_selected_products:
    print(product.text)
    list_ps.append(product.text)
print(list_ps)
assert len(list_ps) > 0
assert len(list_ps) == len(name_products)
assert list_ps == list_products

driver.find_element(By.XPATH,"//button[text()='Place Order']").click()
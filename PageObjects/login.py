from selenium.webdriver.common.by import By


class loginPage:
    def __init__(self,driver):  # constructor in the class that will keep the locators
        self.driver = driver
        self.username_input = (By.ID, "username")  #tupla
        self.password_input = (By.ID, "password")  #tupla
        self.login_button = (By.ID, "signInBtn")   #tupla


    def login(self):
        self.driver.find_element(*self.username_input).send_keys("rahulshettyacademy")
        #è presente l'asterisco perchè find_element vuole 2 argomenti , non la tupla. Con * la tupla si divide in 2 argomenti
        self.driver.find_element(*self.password_input).send_keys("learning")
        self.driver.find_element(*self.login_button).click()
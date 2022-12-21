import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Gmail:
    usrnme = "whsOnd zHQkBf"
    usrnxt = "//*[@id='identifierNext']/div/button/div[3]z"
    pswrd = "//*[@id='password']/div[1]/div/div[1]/input"
    pswdnxt = "//*[@id='passwordNext']/div/button/div[3]"
    compose = "//*[@id=':kr']/div/div"


    def __init__(self,driver):
        self.driver = driver

    def setusername(self, username):
        self.driver.find_element(By.CLASS_NAME, self.usrnme).clear()
        self.driver.find_element(By.CLASS_NAME,self.usrnme).send_keys(username)
        self.driver.find_element(By.XPATH,self.usrnxt).click()

    def setpswdnme(self, password):
        self.driver.find_element(By.XPATH,self.pswrd).clear()
        self.driver.find_element(By.XPATH,self.pswrd).send_keys(password)
        self.driver.find_element(By.XPATH,self.pswdnxt).click()

    def compose(self):
      self.driver.find_element(By.XPATH,self.compose).click()


import selenium
from pageobjects.Login_Page import Gmail
import pytest
from utilities.readfile import readconfig
from utilities.logger import LogGen
import time


class Test_001_Login:
    baseURL = readconfig.getApplicationURL()
    username = readconfig.getusername()
    password = readconfig.getpassword()
    logger=LogGen.loggen()


    def Test_Gmail(self,setup):

     self.logger.info("**** begining the test of gmail ****")
     self.driver  = setup
     self.logger.info("****Opening URL****")
     self.driver.get(self.baseURL)
     time.sleep(4)
     act_title = self.driver.title

     if act_title == "Inbox (2,922) - drumakchinnamech@gmail.com - Gmail":
         self.logger.info("**** Test title test passed ****")
         self.driver.save_screenshot(".\\screenshots\\" + "Test_Gmail.png")
         self.driver.close()
         assert True
     else:
         self.logger.info("**** Home page title test failed****")
         self.driver.close()
         assert False





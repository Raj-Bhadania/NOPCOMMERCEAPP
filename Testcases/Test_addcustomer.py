import random
import string

import pytest
import time

from selenium.webdriver.common.by import By
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen

from PageObjects.LoginPage import Login
from PageObjects.AddCustomer_Page import AddCustomer

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_addcustomer(self,setUp):
        self.logger.info("******** Test_003_AddCustomer ********")
        self.driver = setUp
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(5.0)
        self.driver.maximize_window()
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("*********** Login Successful ***********")
        self.logger.info("********* Starting Add Customer Test ***********")

        self.addcp = AddCustomer(self.driver)
        self.addcp.ClickOnCustomerMenu()
        self.addcp.ClickOnCustomerSubMenu()
        self.addcp.ClickOnAddnew()

        self.logger.info("************ Providing Customer Info *************")
        self.email = random_generator() + "@gmail.com"
        self.addcp.setEmail(self.email)
        self.addcp.setPassword("abc123")
        self.addcp.setFirstName("Micheal")
        self.addcp.setLastName("Bell")
        self.addcp.selectGender('Male')
        self.addcp.setDateOfBirth('07/30/1989')
        self.addcp.setCompanyName("H3-Marris")
        self.addcp.IsTaxExempt('Yes')
        self.addcp.setNewsletter("Test store 2")
       #  self.addcp.setCustomerrole("Vendors")  # Not unteractable through selenium
        self.addcp.isActive(True)
        self.addcp.SaveDetailes()
        self.logger.info("******* Saving Customer Details *********")

        self.logger.info("***** Capturing Customer has been added successfully message *****")
        self.msg = self.driver.find_element(By.XPATH, "(//div[@class='alert alert-success alert-dismissable'])[1]")
        print(self.msg.text)

        try:
            self.logger.info("***** Comparing Message with expected Message *****")
            assert "customer has been added successfully" in self.msg.text
            self.logger.info("***** Add Customer Test Has Been Tested *****")
        except AssertionError:
            self.driver.save_screenshot("ScreenShots/"+"test_addcustomer.png")
            self.logger.error("******* Add Customer Test Failed ********")
            raise
        finally:
            self.driver.close()
            self.logger.info("******* Ending Home Page Title Test ********")


def random_generator(size=8, chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))
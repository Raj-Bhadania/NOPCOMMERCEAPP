import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from PageObjects.LoginPage import Login
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import ExcelUtils


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = '/Users/rajbhadania/PycharmProjects/NOPCOMMERCEAPP/TestData/LoginData.xlsx'
    logger = LogGen.loggen()


    def test_login_DDT(self,setUp):
        self.logger.info("********** Test_002_DDT_Login **********")
        self.logger.info("********** testing Login DDT **********")
        self.driver = setUp
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(4.0)
        self.lp = Login(self.driver)

        Row_Num = ExcelUtils.getRowCount(self.path)
        self.run_status = []

        for r in range(2, Row_Num+1):
            self.username = ExcelUtils.readData(self.path, r, 1)
            self.password = ExcelUtils.readData(self.path, r, 2)
            self.exp = ExcelUtils.readData(self.path, r, 3)
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5.0)
            act_title = self.driver.title
            try:
                assert act_title == 'Dashboard / nopCommerce administration'
                self.logger.info("********** logged in Successfully **********")
                self.status = 'Pass'
                self.lp.clickLogout()
            except AssertionError:
                self.driver.save_screenshot("ScreenShots/"+"test_login.png")
                self.logger.error("********** logged in got failed **********")
                self.status = 'Fail'
            finally:
                if self.status == self.exp:
                    self.run_status.append(True)
                    self.logger.info("********** Expectation is matching with our end result ***********")
                else:
                    self.run_status.append(False)
                    self.logger.info("********** Expectation is not matching, will fail test_login_DDT ***********")
        self.driver.close()
        if False in self.run_status:
            self.logger.info("************** Login DDT Test got failed ******************")
            assert False
        else:
            self.logger.info("************** Login DDT Test got passed ******************")
            assert True

        self.logger.info("**************END of Login DDT Test ******************")
        self.logger.info("************** Completed Test_002_DDT_Login ******************")
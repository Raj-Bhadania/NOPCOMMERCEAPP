import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from PageObjects.LoginPage import Login
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen


class Test_003_Parametrized_Login:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    @pytest.mark.parametrize("username, password",
                             [('admin@yourstore.com', 'admin'),
                              ('admin@yourstore.com', 'adm'),
                              ('adm@yourstore.com', 'admin'),
                              ('adm@yourstore.com', 'adm')])
    def test_login_Parametrized(self, setUp, username, password):
        self.logger.info("********** Test_003_Parametrized_Login **********")
        self.logger.info("********** testing Login Parametrized **********")
        self.driver = setUp
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(4.0)
        self.lp = Login(self.driver)
        self.lp.setUserName(username)
        self.lp.setPassword(password)
        self.lp.clickLogin()
        time.sleep(5.0)
        act_title = self.driver.title
        try:
            assert act_title == 'Dashboard / nopCommerce administration'
            self.logger.info("********** logged in Successfully **********")
            self.lp.clickLogout()
        except AssertionError:
            self.logger.error("********** logged in got failed **********")
            assert False
        self.driver.close()

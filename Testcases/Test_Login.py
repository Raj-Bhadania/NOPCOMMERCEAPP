import pytest

from PageObjects.LoginPage import Login
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()


    def test_homePageTitle(self,setUp):
        self.logger.info("********** Test_001_Login **********")
        self.logger.info("********** Verifying Home Page Title **********")
        self.driver = setUp
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(3.0)
        act_title = self.driver.title
        try:
            assert act_title == 'Your store. Login'
            self.logger.info("********** Home Page Test is Passed **********")
        except AssertionError:
            self.driver.save_screenshot('ScreenShots/'+'test_homepageTitle.png')
            self.logger.error("********** Home Page test is Failed **********")
            assert False
        finally:
            self.driver.close()

    def test_login(self,setUp):
        self.logger.info("********** test_login **********")
        self.logger.info("********** testing Login **********")
        self.driver = setUp
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(4.0)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        try:
            assert act_title == 'Dashboard / nopCommerce administration'
            self.logger.info("********** login test got passed **********")
        except AssertionError:
            self.driver.save_screenshot("ScreenShots/"+"test_login.png")
            self.logger.error("********** login test got failed **********")
            raise
        finally:
            self.driver.close()











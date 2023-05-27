from selenium import webdriver
from selenium.webdriver.common.by import By


class Assertion_Error(Exception):
    msg = "Test Case Got Failed"


class Login:
    textbox_username_xpath = '//*[@id="Email"]'
    textbox_password_xpath = '//*[@id="Password"]'
    button_login_tagname = 'button'
    button_logout_link_text = 'Logout'

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.TAG_NAME, self.button_login_tagname).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.button_logout_link_text).click()


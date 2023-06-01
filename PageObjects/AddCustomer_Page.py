import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class AddCustomer:
    linkcustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    linkcustomers_submennu_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btn_addnew_xpath =  "//a[normalize-space()='Add new']"
    txt_email_xpath =  "//input[@name='Email']"
    txt_password_xpath = "//input[@name='Password']"
    txt_firstname_xpath = "//input[@name='FirstName']"
    txt_lastname_xpath = "//input[@name='LastName']"
    btn_gender_male_xpath = "//input[@id='Gender_Male']"
    btn_gender_female_xpath = "//input[@id='Gender_Female'"
    data_birth_xpath = "//input[@id='DateOfBirth']"
    txt_companyname_xpath = "//input[@name='Company']"
    btn_taxexempt_xpath = "//input[@name='IsTaxExempt']"
    txt_newsletter_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    slct_newsletter_teststore_xpath = "//li[normalize-space()='Test store 2']"
    slct_newsletter_yourstore_xpath = "//li[normalize-space()='Your store name']"
    del_customerrole_xpath = "span[title='delete']"
    guest_customerrole_xpath = "//li[normalize-space()='Guests']"
    administrators_customerrole_xpath = "//li[normalize-space()='Administrators']"
    forum_customerrole_xpath = "//li[normalize-space()='Forum Moderators']"
    vendor_customerrole_xpath = "//li[contains(text(),'Vendors')]"
    btn_active_xpath = "//input[@id='Active']"
    txt_admincomment_xpath = "//textarea[@class='form-control']"
    btn_save_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def ClickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.linkcustomers_menu_xpath).click()

    def ClickOnCustomerSubMenu(self):
        self.driver.find_element(By.XPATH, self.linkcustomers_submennu_xpath).click()

    def ClickOnAddnew(self):
        self.driver.find_element(By.XPATH, self.btn_addnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txt_email_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_email_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH, self.txt_password_xpath).send_keys(password)

    def setFirstName(self,firstname):
        self.driver.find_element(By.XPATH, self.txt_firstname_xpath).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element(By.XPATH, self.txt_lastname_xpath).send_keys(lastname)

    def selectGender(self,gender):
        if gender == 'male' or 'Male':
            self.driver.find_element(By.XPATH, self.btn_gender_male_xpath).click()
        elif gender == 'female' or 'Female':
            self.driver.find_element(By.XPATH, self.btn_gender_female_xpath).click()

    def setDateOfBirth(self,DateOfBirth):
        self.driver.find_element(By.XPATH, self.data_birth_xpath).send_keys(DateOfBirth)

    def setCompanyName(self, company_name):
        self.driver.find_element(By.XPATH, self.txt_companyname_xpath).send_keys(company_name)

    def IsTaxExempt(self, is_exempt):
        if is_exempt == 'yes' or 'Yes':
            self.driver.find_element(By.XPATH, self.btn_taxexempt_xpath).click()

    def setNewsletter(self, newsletter):
        self.driver.find_element(By.XPATH, self.txt_newsletter_xpath).click()
        if newsletter == "Your store name":
            self.driver.find_element(By.XPATH, self.slct_newsletter_yourstore_xpath).click()
        elif newsletter == "Test store 2":
            self.driver.find_element(By.XPATH, self.slct_newsletter_teststore_xpath).click()

    def setCustomerrole(self,customerrole):
        self.driver.find_element(By.CSS_SELECTOR, self.del_customerrole_xpath).click()
        time.sleep(3.0)
        if customerrole == 'Guests':
            self.driver.find_element(By.XPATH, self.guest_customerrole_xpath).click()
        elif customerrole == 'Administrators':
            self.driver.find_element(By.XPATH, self.administrators_customerrole_xpath).click()
        elif customerrole == 'Forum Moderators':
            self.driver.find_element(By.XPATH, self.forum_customerrole_xpath).click()
        elif customerrole == 'Vendors':
            self.driver.find_element(By.XPATH, self.vendor_customerrole_xpath).click()


    def isActive(self, active_boolen):
        if active_boolen == False:
            self.driver.find_element(By.XPATH, self.btn_active_xpath).click()

    def SaveDetailes(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()




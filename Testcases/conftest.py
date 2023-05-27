import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
chrome_driver_path="/Users/rajbhadania/PycharmProjects/chromedriver"
s = Service(chrome_driver_path)


@pytest.fixture()
def setUp():
    driver = webdriver.Chrome(service=s, options=ops)
    return driver


##### Py-test HTML report ########

# it is hook for adding environment info to HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Raj Bhadania'


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)

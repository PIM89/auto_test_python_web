import yaml
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

with open("testdata.yml") as f:
    testdata = yaml.safe_load(f)
    browser = testdata["browser"]


class Site:
    def __init__(self, address):
        if browser == "firefox":
            service = Service(executable_path=GeckoDriverManager().install())
            opt = webdriver.FirefoxOptions()
            self.driver = webdriver.Firefox(service=service, options=opt)
        elif browser == "chrome":
            service = Service(executable_path=ChromeDriverManager().install())
            opt = webdriver.ChromeOptions()
            self.driver = webdriver.Chrome(service=service, options=opt)
        self.driver.implicitly_wait(testdata["wait"])
        self.driver.maximize_window()
        self.driver.get(address)
        time.sleep(testdata["sleep_time"])

    def find_element(self, mode, path):
        if mode == "css":
            elem = self.driver.find_element(By.CSS_SELECTOR, path)
        elif mode == "xpath":
            elem = self.driver.find_element(By.XPATH, path)
        else:
            elem = None
        return elem

    def get_element_property(self, mode, path, property_elem):
        elem = self.find_element(mode, path)
        return elem.value_of_css_property(property_elem)

    def refresh(self):
        self.driver.refresh()

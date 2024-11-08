import logging

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://test-stand.gb.ru"

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def get_element_property(self, locator, property):
        element = self.find_elements(locator)
        return element.get_property(property)

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def to_alert(self):
        try:
            alert = self.driver.switch_to.alert
            return alert.text
        except:
            logging.exception("Exception with alert")
            return None

    def quit(self):
        self.driver.quit()

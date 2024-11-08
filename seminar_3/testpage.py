import logging

import yaml

from BaseApp import BasePage
from selenium.webdriver.common.by import By

with open("./testdata.yml") as f:
    data = yaml.safe_load(f)


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = By.XPATH, """//*[@id="login"]/div[1]/label/input"""
    LOCATOR_PASS_FIELD = By.XPATH, """//*[@id="login"]/div[2]/label/input"""
    LOCATOR_LOGIN_BTN = By.CSS_SELECTOR, """button"""
    LOCATOR_ERROR_FIELD = By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2"""
    LOCATOR_HELLO = By.XPATH, """//*[@id="app"]/main/nav/ul/li[3]/a"""

    LOCATOR_NEW_POST_BTN = By.XPATH, """//*[@id="create-btn"]"""
    LOCATOR_TITLE_FIELD = By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input"""
    LOCATOR_DESCRIPTION_FIELD = By.XPATH, """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""
    LOCATOR_CONTENT_FIELD = By.XPATH, """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""
    LOCATOR_SAVE_NEW_POST_BTN = By.XPATH, """//*[@id="create-item"]/div/div/div[7]/div/button/span"""
    LOCATOR_NEW_POST_TITLE_FIELD = By.XPATH, """//*[@id="app"]/main/div/div[1]/h1"""

    LOCATOR_HOME_BTN = By.XPATH, """//*[@id="app"]/main/nav/a/span"""
    LOCATOR_CONTACT_BTN = By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a"""
    LOCATOR_CONTACT_US_TEXT = By.XPATH, """//*[@id="app"]/main/div/div/h1"""
    LOCATOR_CONTACT_US_NAME_FIELD = By.XPATH, """//*[@id="contact"]/div[1]/label/input"""
    LOCATOR_CONTACT_US_EMAIL_FIELD = By.XPATH, """//*[@id="contact"]/div[2]/label/input"""
    LOCATOR_CONTACT_US_CONTENT_FIELD = By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea"""
    LOCATOR_CONTACT_US_SEND_FORM_BTN = By.CSS_SELECTOR, """#contact > div.submit > button"""


class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f"Send '{word}' to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_elements(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        login_field = self.find_elements(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def click_login_button(self):
        self.find_elements(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        return self.find_elements(TestSearchLocators.LOCATOR_ERROR_FIELD, time=2).text

    def get_user_text(self):
        return self.find_elements(TestSearchLocators.LOCATOR_HELLO, time=2).text

    def click_new_post(self):
        self.find_elements(TestSearchLocators.LOCATOR_NEW_POST_BTN).click()

    def enter_title(self, text):
        field = self.find_elements(TestSearchLocators.LOCATOR_TITLE_FIELD)
        field.clear()
        field.send_keys(text)

    def enter_description(self, text):
        field = self.find_elements(TestSearchLocators.LOCATOR_DESCRIPTION_FIELD)
        field.clear()
        field.send_keys(text)

    def enter_content(self, text):
        field = self.find_elements(TestSearchLocators.LOCATOR_CONTENT_FIELD)
        field.clear()
        field.send_keys(text)

    def click_save_post(self):
        self.find_elements(TestSearchLocators.LOCATOR_SAVE_NEW_POST_BTN).click()

    def get_new_post_title(self):
        return self.find_elements(TestSearchLocators.LOCATOR_NEW_POST_TITLE_FIELD, time=2).text

    def click_home_btn(self):
        self.find_elements(TestSearchLocators.LOCATOR_HOME_BTN).click()

    def click_contact_btn(self):
        self.find_elements(TestSearchLocators.LOCATOR_CONTACT_BTN).click()

    def get_contact_us_text(self):
        return self.find_elements(TestSearchLocators.LOCATOR_CONTACT_US_TEXT).text

    def enter_name_contact(self, word):
        field = self.find_elements(TestSearchLocators.LOCATOR_CONTACT_US_NAME_FIELD)
        field.clear()
        field.send_keys(word)

    def get_name_field(self):
        return self.get_element_property(TestSearchLocators.LOCATOR_CONTACT_US_NAME_FIELD, "value")

    def enter_email_contact(self, word):
        field = self.find_elements(TestSearchLocators.LOCATOR_CONTACT_US_EMAIL_FIELD)
        field.clear()
        field.send_keys(word)

    def get_email_field(self):
        return self.get_element_property(TestSearchLocators.LOCATOR_CONTACT_US_EMAIL_FIELD, "value")

    def enter_content_contact(self, word):
        field = self.find_elements(TestSearchLocators.LOCATOR_CONTACT_US_CONTENT_FIELD)
        field.clear()
        field.send_keys(word)

    def get_content_field(self):
        return self.get_element_property(TestSearchLocators.LOCATOR_CONTACT_US_CONTENT_FIELD, "value")

    def click_send_form_bth(self):
        self.find_elements(TestSearchLocators.LOCATOR_CONTACT_US_SEND_FORM_BTN).click()

    def get_alert(self):
        text = self.to_alert()
        return text
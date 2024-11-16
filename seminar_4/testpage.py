import logging

import yaml

from BasePage import BasePage
from selenium.webdriver.common.by import By


class TestSearchLocators:
    ids = dict()
    with open("locators.yml") as f:
        locators = yaml.safe_load(f)

    for locator in locators["xpath"]:
        ids[locator] = By.XPATH, locators["xpath"][locator]

    for locator in locators["css"]:
        ids[locator] = By.CSS_SELECTOR, locators["css"][locator]


class OperationsHelper(BasePage):
    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send {word} to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with {locator}")
            return False
        return True

    def button_click(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception with click")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get text from {element_name}")
            return None
        logging.info(f"We find text {text} in field {element_name}")
        return text

    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"], word,
                                   description=f"Enter login: {word}")

    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_PASS_FIELD"], word,
                                   description=f"Enter password: {word}")

    def click_login_button(self):
        self.button_click(TestSearchLocators.ids["LOCATOR_LOGIN_BTN"], description=f"Click login button")

    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_ERROR_FIELD"], description="Get text error")

    def get_user_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_HELLO"], description="Get user text HELLO!")

    def click_new_post(self):
        self.button_click(TestSearchLocators.ids["LOCATOR_NEW_POST_BTN"], description="Click new post")

    def enter_title(self, text):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_TITLE_FIELD"], text,
                                   description=f"Enter title: {text}")

    def enter_description(self, text):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_DESCRIPTION_FIELD"], text,
                                   description=f"Enter description: {text}")

    def enter_content(self, text):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTENT_FIELD"], text,
                                   description=f"Enter content: {text}")

    def click_save_post(self):
        self.button_click(TestSearchLocators.ids["LOCATOR_SAVE_NEW_POST_BTN"], description="Click save post")

    def get_new_post_title(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_NEW_POST_TITLE_FIELD"],
                                   description="Get new post title")

    def click_home_btn(self):
        self.button_click(TestSearchLocators.ids["LOCATOR_HOME_BTN"], description="Click 'HOME'")

    def click_contact_btn(self):
        self.button_click(TestSearchLocators.ids["LOCATOR_CONTACT_BTN"], description="Click contact button")

    def get_contact_us_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_CONTACT_US_TEXT"], description="Get contact us text")

    def enter_name_contact(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTACT_US_NAME_FIELD"], word,
                                   description=f"Enter name: {word}")

    def get_name_field(self):
        return self.get_element_property(TestSearchLocators.ids["LOCATOR_CONTACT_US_NAME_FIELD"], "value")

    def enter_email_contact(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTACT_US_EMAIL_FIELD"], word,
                                   description=f"Enter email: {word}")

    def get_email_field(self):
        return self.get_element_property(TestSearchLocators.ids["LOCATOR_CONTACT_US_EMAIL_FIELD"], "value")

    def enter_content_contact(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTACT_US_CONTENT_FIELD"], word,
                                   description=f"Enter content: {word}")

    def get_content_field(self):
        return self.get_element_property(TestSearchLocators.ids["LOCATOR_CONTACT_US_CONTENT_FIELD"], "value")

    def click_send_form_bth(self):
        self.button_click(TestSearchLocators.ids["LOCATOR_CONTACT_US_SEND_FORM_BTN"], description="Click send form")

    def get_alert(self):
        return self.get_alert_text()

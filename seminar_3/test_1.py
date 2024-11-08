import logging
import time

import lorem

from testpage import OperationsHelper
import yaml

with open("./testdata.yml") as f:
    data = yaml.safe_load(f)


def create_post_information():
    title = lorem.get_word(count=1)
    description = lorem.get_word(count=3)
    content = lorem.get_sentence(count=5)
    return title, description, content


def create_contact_information():
    name = lorem.get_word(count=1)
    email = f'{lorem.get_word(count=1)}@mail.ru'
    content = lorem.get_sentence(count=1)
    return name, email, content

def test_step1(browser):
    logging.info("Test 1 start")
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    test_page.enter_login("test")
    test_page.enter_pass("test")
    test_page.click_login_button()
    error_text = test_page.get_error_text()
    assert error_text == "401"


def test_step2(browser):
    logging.info("Test 2 start")
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    test_page.enter_login(data["username"])
    test_page.enter_pass(data["password"])
    test_page.click_login_button()
    assert test_page.get_user_text() == f"Hello, {data["username"]}"


def test_step3(browser):
    logging.info("Test 3 start")
    test_page = OperationsHelper(browser)
    test_page.click_new_post()
    title, description, content = create_post_information()
    test_page.enter_title(title)
    test_page.enter_description(description)
    test_page.enter_content(content)
    test_page.click_save_post()
    time.sleep(2)
    assert test_page.get_new_post_title() == title


def test4(browser):
    logging.info("Test 4. Start...")
    test_page = OperationsHelper(browser)
    test_page.click_home_btn()
    test_page.click_contact_btn()
    name, email, content = create_contact_information()
    test_page.enter_name_contact(name)
    test_page.enter_email_contact(email)
    test_page.enter_content_contact(content)
    test_page.click_send_form_bth()
    time.sleep(2)
    alert_text = test_page.get_alert()
    logging.info(f"Test 4. Alert text: {alert_text}")
    assert "Form successfully submitted" in alert_text

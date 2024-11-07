import time

import yaml
from module import Site

with open("./testdata.yml") as f:
    data = yaml.safe_load(f)


def test_step1(x_selector_username, x_selector_passwd, x_selector_err_auth, btn_selector_auth, err_auth_text):
    site = Site(data["address"])
    input1 = site.find_element("xpath", x_selector_username)
    input1.send_keys("test")
    input2 = site.find_element("xpath", x_selector_passwd)
    input2.send_keys("test")
    bth = site.find_element("css", btn_selector_auth)
    bth.click()
    err_label = site.find_element("xpath", x_selector_err_auth)
    text = err_label.text
    site.close()
    assert text == err_auth_text


def test_step2(authorization, x_selector_success_auth, success_auth_text):
    site = authorization
    label = site.find_element("xpath", x_selector_success_auth)
    text = label.text
    site.close()
    assert text == success_auth_text


def test_step3(authorization, bth_selector_add_post, x_selector_title, x_selector_description, x_selector_content,
               bth_selector_create_post, create_post_information, x_selector_create_title):
    site = authorization
    bth = site.find_element("xpath", bth_selector_add_post)
    bth.click()

    title_elem = site.find_element("xpath", x_selector_title)
    description_elem = site.find_element("xpath", x_selector_description)
    content_elem = site.find_element("xpath", x_selector_content)
    bth = site.find_element("xpath", bth_selector_create_post)

    title_text, description_text, content_text = create_post_information
    title_elem.send_keys(title_text)
    description_elem.send_keys(description_text)
    content_elem.send_keys(content_text)
    bth.click()
    time.sleep(data["sleep_time"])

    create_post_title = site.find_element("xpath", x_selector_create_title)
    assert create_post_title.text == title_text
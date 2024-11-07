import lorem

from module import Site

import pytest
import yaml

with open("./testdata.yml") as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def authorization(x_selector_username, x_selector_passwd, btn_selector_auth):
    site = Site(data["address"])
    input1 = site.find_element("xpath", x_selector_username)
    input1.clear()
    input1.send_keys(data["username"])
    input2 = site.find_element("xpath", x_selector_passwd)
    input2.clear()
    input2.send_keys(data["password"])
    bth = site.find_element("css", btn_selector_auth)
    bth.click()
    return site


# Авторизация на сайте

@pytest.fixture()
def x_selector_username():
    return """//*[@id="login"]/div[1]/label/input"""


@pytest.fixture()
def x_selector_passwd():
    return """//*[@id="login"]/div[2]/label/input"""


@pytest.fixture()
def x_selector_err_auth():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""


@pytest.fixture()
def err_auth_text():
    return "401"


@pytest.fixture()
def x_selector_success_auth():
    return """//*[@id="app"]/main/nav/ul/li[3]/a"""


@pytest.fixture()
def success_auth_text():
    return f"Hello, {data["username"]}"


@pytest.fixture()
def btn_selector_auth():
    return """button"""


# Добавление поста

@pytest.fixture()
def bth_selector_add_post():
    return """//*[@id="create-btn"]"""


@pytest.fixture()
def x_selector_title():
    return """//*[@id="create-item"]/div/div/div[1]/div/label/input"""


@pytest.fixture()
def x_selector_description():
    return """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""


@pytest.fixture()
def x_selector_content():
    return """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""

@pytest.fixture()
def x_selector_create_title():
    return """//*[@id="app"]/main/div/div[1]/h1"""

@pytest.fixture()
def bth_selector_create_post():
    return """//*[@id="create-item"]/div/div/div[7]/div/button"""


@pytest.fixture()
def create_post_information():
    title = lorem.get_word(count=data["length_title"])
    description = lorem.get_word(count=data["length_description"])
    content = lorem.get_sentence(count=data["length_content"])
    return title, description, content
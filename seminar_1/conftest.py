import pytest
import requests
import yaml
import lorem

with open("config.yaml") as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def login():
    result = requests.post(data["address"] + "/gateway/login",
                           data={"username": data["username"], "password": data["password"]})
    return result.json()["token"]


@pytest.fixture()
def test_text():
    return "Тестовый заголовок"

@pytest.fixture()
def create_post_information():
    title = lorem.get_word(count=1)
    description = lorem.get_word(count=3)
    content = lorem.get_sentence(count=5)
    return title, description, content

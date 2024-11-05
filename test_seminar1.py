import requests
import yaml


with open("config.yaml") as f:
    data = yaml.safe_load(f)


def test_step1(login, test_text):
    header = {"X-Auth-Token": login}
    result = requests.get(data["address"] + "/api/posts", params={"owner": "notMe"}, headers=header)
    listres = [i["title"] for i in result.json()["data"]]
    print(listres)
    assert test_text in listres


def test_step2(login, create_post_information):
    title_post, description, content = create_post_information
    header = {"X-Auth-Token": login}
    result = requests.post(data["address"] + "/api/posts",
                           data={"title": title_post, "description": description, "content": content}, headers=header)
    assert description == result.json()["description"]

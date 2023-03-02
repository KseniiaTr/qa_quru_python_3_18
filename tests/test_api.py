import os

from dotenv import load_dotenv
from pytest_voluptuous import S
from requests import Response


from tests.schemas.schema import resource_list_schema
from tests.utils.base_session import BaseSession

load_dotenv()
REGRES_URL = os.getenv("REGRES_URL")

regres = BaseSession(REGRES_URL)

def test_assert_code_status():
    response: Response = regres.get("/unknown")
    print(response)
    assert response.status_code == 200


def test_assert_response():
    response: Response = regres.get("/unknown/2")
    print(response.json())
    assert response.json().get('data').get('pantone_value')


def test_assert_response():
    response: Response = regres.get("/unknown/2")
    print(response.json())

    assert response.status_code == 200
    assert response.json()['data']['pantone_value'] == '17-2031'


def test_assert_number_of_letters():
    response: Response = regres.get("/unknown/2")

    color = response.json().get('data').get('pantone_value')
    print(color)
    assert len(response.content) == 232


def test_schema_resource_list():
    result = regres.get("/unknown", params={"page": 4})

    assert S(resource_list_schema) == result.json()


def test_number_of_page():
    response: Response = regres.get("/unknown")

    page = response.json().get("per_page")

    assert page == 6


def test_register():

    result = regres.post("/register", data={"email": "user123@gmail.com",
                                                                       "password": "Qwerty123"})

    print(result)
    assert result.status_code == 400


def test_assert_data():
    response: Response = regres.get("/unknown/2")

    assert response.json().get("data").get("name") == "fuchsia rose"


def test_test_choose():
    response: Response = regres.get("/unknown/2")
    print(response.status_code)
    name = response.json().get("data").get("year")
    print(name)
    assert len(response.content) != 0

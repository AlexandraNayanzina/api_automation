import jsonpath
import pytest
import requests
import json

url = "https://reqres.in/api/users"
file_name = "tests/UserData.json"

@pytest.fixture(scope='module')
def sending_request():
    print('FIXTURE')
    global response
    file = open(file_name, "r")
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)

def test_create_user(sending_request):
    print("The body of the 01 test")
    # Validating the response code
    assert response.status_code == 201, "The response code is wrong"


def test_create_user_and_fetch_userdata(sending_request):
    print("The body of the 02 test")
    # Converting body to the JSON format
    response_json = json.loads(response.text)
    # Getting "id" using jsonpath
    id_field = jsonpath.jsonpath(response_json, "id")
    print(id_field[0])

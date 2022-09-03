import requests
import json
import jsonpath

def test_update_student_data():
    # Given
    url = 'https://thetestingworldapi.com/api/studentsDetails/2678942'
    file = open('tests/student_update_info.json', 'r')
    json_input = file.read()
    request_json = json.loads(json_input)

    # When
    response = requests.put(url, request_json)
    print()
    print(response.content)
    print(response.status_code)

    # # Verify response body
    # response_json = json.loads(response.text)
    # assert len(response_json) == 5, "The number of filed in response body IS NOT correct"
    #
    # # id_field = jsonpath.jsonpath(response_json, 'id')
    # # assert id_field[0] == 2678943, 'The "id" IS NOT correct'
    #
    # first_name_field = jsonpath.jsonpath(response_json, 'first_name')
    # assert first_name_field[0] == 'A', 'The "first_name" IS NOT correct'
    #
    # middle_name_field = jsonpath.jsonpath(response_json, 'middle_name')
    # assert middle_name_field[0] == 'B', 'The "middle_name" IS NOT correct'
    #
    # last_name_field = jsonpath.jsonpath(response_json, 'last_name')
    # assert last_name_field[0] == 'Test', 'The "last_name" IS NOT correct'
    #
    # date_of_birth_field = jsonpath.jsonpath(response_json, 'date_of_birth')
    # assert date_of_birth_field[0] == '01-01-1986', 'The "date_of_birth" IS NOT correct'










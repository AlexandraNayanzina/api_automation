import requests
import json
import jsonpath

def test_add_student_data():
    # Given
    url = 'https://thetestingworldapi.com/api/studentsDetails'
    file = open('tests/student_info.json', 'r')
    json_input = file.read()
    request_json = json.loads(json_input)

    # When
    response = requests.post(url, request_json)
    print()
    print(response.text)

    # Then
    assert response.status_code == 201, "The response status code IS NOT correct"

    # Verify response body
    response_json = json.loads(response.text)
    assert len(response_json) == 5, "The number of filed in response body IS NOT correct"

    first_name_field = jsonpath.jsonpath(response_json, 'first_name')
    assert first_name_field[0] == 'A', 'The "first_name" IS NOT correct'

    middle_name_field = jsonpath.jsonpath(response_json, 'middle_name')
    assert middle_name_field[0] == 'B', 'The "middle_name" IS NOT correct'

    last_name_field = jsonpath.jsonpath(response_json, 'last_name')
    assert last_name_field[0] == 'Test', 'The "last_name" IS NOT correct'

    date_of_birth_field = jsonpath.jsonpath(response_json, 'date_of_birth')
    assert date_of_birth_field[0] == '01-01-1986', 'The "date_of_birth" IS NOT correct'

# def test_fetch_student_details():
#     url_particular_student = 'https://thetestingworldapi.com/api/studentsDetails/2678942'
#     # When
#     response = requests.get(url_particular_student)
#     # Then
#     assert response.status_code == 200, 'Response status code is NOT correct'
#     response_json = json.loads(response.text)
#     id_student = jsonpath.jsonpath(response_json, 'id')
#     assert id_student[0] == 2678942, 'The id is NOT correct'








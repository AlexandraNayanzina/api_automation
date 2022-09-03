import requests
import json
import jsonpath

url_all_students = 'https://thetestingworldapi.com/api/studentsDetails'
url_particular_student = 'https://thetestingworldapi.com/api/studentsDetails/2678942'

def test_fetch_all_student_details():
    # When
    response = requests.get(url_all_students)
    # Then
    assert response.status_code == 200, 'Response status code is NOT correct'
    response_json = json.loads(response.text)
    for student in response_json:
        print(student)
    print(len(response_json), type(response_json))

def test_fetch_particular_student_details():
    # When
    response = requests.get(url_particular_student)
    # Then
    assert response.status_code == 200, 'Response status code is NOT correct'
    response_json = json.loads(response.text)
    print()
    print(response_json)
    status_data_student = jsonpath.jsonpath(response_json, 'status')
    assert status_data_student[0] == 'false', 'The status is NOT correct'








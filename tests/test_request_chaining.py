import requests
import json
import jsonpath

def test_add_new_student():
    global id_student
    url = 'https://thetestingworldapi.com/api/studentsDetails'
    file = open('tests/student_info.json','r')
    request_json = json.loads(file.read())
    response_student = requests.post(url, request_json)
    response_student_json = response_student.json()
    id_student = jsonpath.jsonpath(response_student_json, 'id')
    print()
    print('Student id: ',id_student[0])


def test_get_student_details():
    url_details = 'https://thetestingworldapi.com/api/studentsDetails/'+ str(id_student[0])
    response_details = requests.get(url_details)
    print(response_details.text)
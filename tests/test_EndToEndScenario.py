import requests
import json
import jsonpath


def test_end_to_end():
    # Add new Student
    url = 'https://thetestingworldapi.com/api/studentsDetails'
    file = open('tests/student_info.json', 'r')
    request_json_student = json.loads(file.read())
    response_student = requests.post(url, request_json_student)
    response_student_json = response_student.json()
    assert response_student.status_code == 201, "The response status code of --create student-- request IS NOT correct"
    first_name_student_data = jsonpath.jsonpath(response_student_json, 'first_name')
    id_student_data = jsonpath.jsonpath(response_student_json, 'id')
    print(id_student_data[0])
    assert first_name_student_data[0] == 'A', 'The "first_name" field is NOT correct'

    # Add new Tech Skill for Student
    url_create_tech_skill = 'https://thetestingworldapi.com/api/technicalskills'
    file_tech_skills = open('tests/tech_skills.json', 'r')
    request_json_skills = json.loads(file_tech_skills.read())
    response_skills = requests.post(url_create_tech_skill, request_json_skills)
    print(response_skills.text)
    response_skills_json = json.loads(response_skills.text)
    response_skills_json['id'] = int(id_student_data[0])
    response_skills_json['st_id'] = id_student_data[0]
    assert response_skills.status_code == 200, "The response status code of --add tech skills-- request IS NOT correct"
    status_data = jsonpath.jsonpath(response_skills_json, 'status')
    assert status_data[0] == 'true', 'The "status" in the address is NOT match the expected result'

    # Add new Address
    url_address = 'https://thetestingworldapi.com/api/addresses'
    file_address = open('tests/address.json', 'r')
    request_address_json = json.loads(file_address.read())
    response_address = requests.post(url_address, request_address_json)
    response_address_json = response_address.json()
    response_skills_json['stId'] = int(id_student_data[0])
    assert response_skills.status_code == 200, "The response status code of --add address-- request IS NOT correct"
    status_data = jsonpath.jsonpath(response_address_json, 'status')
    assert status_data[0] == 'true', 'The "status" in the address is NOT match the expected result'


    # Fetch All Student Details
    url_all_details = 'https://thetestingworldapi.com/api/FinalStudentDetails/'+ str(id_student_data[0])
    response_all_details = requests.get(url_all_details)
    response_all_details_json = response_all_details.json()
    assert response_all_details.status_code == 200, "The response status code of --get all details-- request IS NOT correct"
    print(response_all_details_json)



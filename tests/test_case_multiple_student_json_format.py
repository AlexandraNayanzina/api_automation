import requests
import json
import jsonpath


def test_create_multiple_student_from_json_format():
    url = 'https://thetestingworldapi.com/api/studentsDetails'
    file = open('tests/student_data.json', 'r')
    request_json = json.loads(file.read())
    print()

    # Open and read data from JSON file
    file_students = open('tests/student_data_multiple.json', 'r')
    multiple_student_dict = json.loads(file_students.read())

    row_num = len(multiple_student_dict['students'])
    print('Number of students', row_num)

    data_first_name = multiple_student_dict['students'][0]['first_name']
    print(data_first_name)

    for i in range(row_num):
        request_json['first_name'] = multiple_student_dict['students'][i]['first_name']
        request_json['middle_name']  = multiple_student_dict['students'][i]['middle_name']
        request_json['last_name'] = multiple_student_dict['students'][i]['last_name']
        request_json['date_of_birth'] = multiple_student_dict['students'][i]['date_of_birth']

        # Send POST request and print out the response
        response = requests.post(url, request_json)
        print()
        print(response.text)

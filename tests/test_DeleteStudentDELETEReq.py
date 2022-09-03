import requests

url = 'https://thetestingworldapi.com/api/studentsDetails/2678942'

def test_delete_student_data():
    response = requests.delete(url)


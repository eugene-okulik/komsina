import requests

BASE_URL = 'http://objapi.course.qa-practice.com/object'
HEADERS = {'Content-Type': 'application/json'}


class GetObject:
    def get_object_by_id(self, object_id):
        return requests.get(f'{BASE_URL}/{object_id}', headers=HEADERS)

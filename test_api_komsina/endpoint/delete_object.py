import requests

BASE_URL = 'http://objapi.course.qa-practice.com/object'
HEADERS = {'Content-Type': 'application/json'}


class DeleteObject:
    def delete_object(self, object_id):
        return requests.delete(f'{BASE_URL}/{object_id}', headers=HEADERS)

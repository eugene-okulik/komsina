import requests

BASE_URL = 'http://objapi.course.qa-practice.com/object'
HEADERS = {'Content-Type': 'application/json'}


class PatchObject:
    def partial_update_object(self, object_id, name):
        body = {
            'name': name
        }
        return requests.patch(f'{BASE_URL}/{object_id}', json=body, headers=HEADERS)

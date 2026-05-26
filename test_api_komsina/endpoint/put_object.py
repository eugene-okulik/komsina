import requests

BASE_URL = 'http://objapi.course.qa-practice.com/object'
HEADERS = {'Content-Type': 'application/json'}


class PutObject:
    def update_object(self, object_id, name, color, size):
        body = {
            'name': name,
            'data': {
                'color': color,
                'size': size
            }
        }
        return requests.put(f'{BASE_URL}/{object_id}', json=body, headers=HEADERS)

    def update_object_without_name(self, object_id, color, size):
        body = {
            'data': {
                'color': color,
                'size': size
            }
        }
        return requests.put(f'{BASE_URL}/{object_id}', json=body, headers=HEADERS)

    def update_object_without_data(self, object_id, name):
        body = {
            'name': name
        }
        return requests.put(f'{BASE_URL}/{object_id}', json=body, headers=HEADERS)

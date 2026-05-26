import requests

BASE_URL = 'http://objapi.course.qa-practice.com/object'
HEADERS = {'Content-Type': 'application/json'}


class PostObject:
    def create_object(self, name, color, size):
        body = {
            'name': name,
            'data': {
                'color': color,
                'size': size
            }
        }
        return requests.post(BASE_URL, json=body, headers=HEADERS)

    def create_object_without_name(self, color, size):
        body = {
            'data': {
                'color': color,
                'size': size
            }
        }
        return requests.post(BASE_URL, json=body, headers=HEADERS)

    def create_object_without_data(self, name):
        body = {
            'name': name
        }
        return requests.post(BASE_URL, json=body, headers=HEADERS)

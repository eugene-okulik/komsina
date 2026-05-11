import pytest
import requests


@pytest.fixture()
def new_object_id():
    body = {
        "name": "test",
        "data": {
            "color": "test color",
            "size": "test size"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://objapi.course.qa-practice.com/object', json=body,
                             headers=headers)
    object_id = response.json()['id']
    yield object_id
    requests.delete(
        f'http://objapi.course.qa-practice.com/object/{object_id}')


@pytest.fixture(scope="session")
def inform_about_start_and_end_testing():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture(scope="function")
def inform_about_start_and_end_of_each_test():
    print('before test')
    yield
    print(' after test')

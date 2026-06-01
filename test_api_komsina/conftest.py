import pytest
from endpoint.post_object import PostObject
from endpoint.delete_object import DeleteObject
from endpoint.get_object import GetObject
from endpoint.put_object import PutObject
from endpoint.patch_object import PatchObject
from test_data import DEFAULT_NAME, DEFAULT_COLOR, DEFAULT_SIZE
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


@pytest.fixture()
def post_object():
    return PostObject()


@pytest.fixture()
def delete_object():
    return DeleteObject()


@pytest.fixture()
def get_object():
    return GetObject()


@pytest.fixture()
def put_object():
    return PutObject()


@pytest.fixture()
def patch_object():
    return PatchObject()


@pytest.fixture()
def existing_object(post_object, delete_object):
    body = {
        'name': DEFAULT_NAME,
        'data': {
            'color': DEFAULT_COLOR,
            'size': DEFAULT_SIZE
        }
    }
    post_object.create_object(body)
    assert post_object.response.status_code == 200, (
        f'Не удалось создать объект для теста. '
        f'Статус: {post_object.response.status_code}, '
        f'тело: {post_object.response.text}'
    )
    object_data = post_object.response.json()
    yield object_data

    delete_object.delete_object(object_data['id'])

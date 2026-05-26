import sys
import os
import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from endpoint.post_object import PostObject
from endpoint.delete_object import DeleteObject

post_object = PostObject()
delete_object = DeleteObject()

DEFAULT_NAME = 'test object'
DEFAULT_COLOR = 'test color'
DEFAULT_SIZE = 'test size'


@pytest.fixture()
def existing_object():
    response = post_object.create_object(
        name=DEFAULT_NAME,
        color=DEFAULT_COLOR,
        size=DEFAULT_SIZE
    )
    assert response.status_code == 200, (
        f'Не удалось создать объект для теста. '
        f'Статус: {response.status_code}, тело: {response.text}'
    )
    object_data = response.json()
    yield object_data

    delete_object.delete_object(object_data['id'])
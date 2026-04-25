import requests

# Получить все объекты
# def get_objects():
#     response = requests.get('http://objapi.course.qa-practice.com/object')
#     # print(response)
#     assert response.status_code == 200, 'Status code is not correct'
#     assert response is not None, 'Response is None'

# Создать новый объект
def post_new_object():
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
    return response.json()['id']

# Очистка после создания
def clear(object_id):
    response = requests.delete(
        f'http://objapi.course.qa-practice.com/object/{object_id}')

# Получить объект по id
# def get_object_by_id():
#     object_id = post_new_object()
#     response = requests.get(
#         f'http://objapi.course.qa-practice.com/object/{object_id}').json()
#     assert response['id'] == object_id
#     clear(object_id)

# Проверка создания объекта
def verify_post_new_object():
    expected_name = "test AT 2"
    body = {"name": expected_name, "data": {"color": "test color", "size": "test size"}}
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://objapi.course.qa-practice.com/object',
                             json=body, headers=headers)
    object_id = response.json()['id']
    assert response.status_code == 200, f'Expected 200, got {response.status_code}'
    assert response.json()[
               'name'] == expected_name, f'Expected name {expected_name}, got {response.json()["name"]}'
    response_no_name = requests.post('http://objapi.course.qa-practice.com/object',
                                     json={"data": body["data"]},
                                     headers=headers)
    assert response_no_name.status_code == 400, f'Expected 400, got {response_no_name.status_code}'
    response_no_data = requests.post('http://objapi.course.qa-practice.com/object',
                                     json={"name": body["name"]},
                                     headers=headers)
    assert response_no_data.status_code == 400, f'Expected 400, got {response_no_data.status_code}'
    clear(object_id)

# Проверка изменения существующего объекта методом PUT
def verify_put_object():
    expected_name = "test updated"
    body = {"name": expected_name,
            "data": {"color": "test color updated", "size": "test size updated"}}
    headers = {'Content-Type': 'application/json'}
    object_id = post_new_object()
    response = requests.put(f'http://objapi.course.qa-practice.com/object/{object_id}',
                            json=body, headers=headers)
    assert response.status_code == 200, f'Expected 200, got {response.status_code}'
    assert response.json()['name'] == expected_name, f'Expected name {expected_name}, got {response.json()["name"]}'
    assert response.json()['data'] == body['data'], f'Expected data {body["data"]}, got {response.json()["data"]}'
    response_no_name = requests.put(
        f'http://objapi.course.qa-practice.com/object/{object_id}',
        json={"data": body["data"]},
        headers=headers)
    assert response_no_name.status_code == 400, f'Expected 400, got {response_no_name.status_code}'
    response_no_data = requests.put(
        f'http://objapi.course.qa-practice.com/object/{object_id}',
        json={"name": body["name"]},
        headers=headers)
    assert response_no_data.status_code == 400, f'Expected 400, got {response_no_data.status_code}'
    clear(object_id)

# Проверка изменения существующего объекта методом PATCH
def verify_patch_object():
    expected_name = "test updated 2"
    body = {"name": expected_name}
    headers = {'Content-Type': 'application/json'}
    object_id = post_new_object()
    response = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{object_id}',
        json=body, headers=headers)
    assert response.status_code == 200, f'Expected 200, got {response.status_code}'
    assert response.json()[
               'name'] == expected_name, f'Expected name {expected_name}, got {response.json()["name"]}'
    assert response.json()[
               'id'] == object_id, f'Expected id {object_id}, got {response.json()["id"]}'
    clear(object_id)

# Проверка удаления объекта
def verify_delete_object():
    object_id = post_new_object()
    response = requests.delete(
        f'http://objapi.course.qa-practice.com/object/{object_id}')
    assert response.status_code == 200, f'Expected 200, got {response.status_code}'
    assert f'Object with id {object_id} successfully deleted' in response.text, \
        f'Expected deletion message, got {response.text}'
    response_not_found = requests.delete(
        'http://objapi.course.qa-practice.com/object/99999999999')
    assert response_not_found.status_code == 404, f'Expected 404, got {response_not_found.status_code}'

verify_post_new_object()
verify_put_object()
verify_patch_object()
verify_delete_object()

import pytest
import requests
import allure


@allure.title('Получение объекта по id')
@allure.feature('Get data')
@allure.story('Get')
@pytest.mark.medium
def test_get_object_by_id(new_object_id, inform_about_start_and_end_testing,
                          inform_about_start_and_end_of_each_test):
    response = requests.get(
        f'http://objapi.course.qa-practice.com/object/{new_object_id}').json()
    assert response['id'] == new_object_id


@pytest.mark.parametrize('expected_name',
                         ['expected_name_1', 'expected_name_2', 'expected_name_3'])
@pytest.mark.critical
def test_verify_post_new_object(new_object_id, expected_name,
                                inform_about_start_and_end_of_each_test):
    body = {"name": expected_name, "data": {"color": "test color", "size": "test size"}}
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://objapi.course.qa-practice.com/object',
                             json=body, headers=headers)
    assert response.status_code == 200, f'Expected 200, got {response.status_code}'
    assert response.json()['name'] == expected_name, \
        f'Expected name {expected_name}, got {response.json()["name"]}'
    response_no_name = requests.post('http://objapi.course.qa-practice.com/object',
                                     json={"data": body["data"]},
                                     headers=headers)
    assert response_no_name.status_code == 400, f'Expected 400, got {response_no_name.status_code}'
    response_no_data = requests.post('http://objapi.course.qa-practice.com/object',
                                     json={"name": body["name"]},
                                     headers=headers)
    assert response_no_data.status_code == 400, f'Expected 400, got {response_no_data.status_code}'


@allure.feature('Update data')
@allure.story('Update')
def test_verify_put_object(new_object_id, inform_about_start_and_end_of_each_test):
    expected_name = "test updated"
    body = {"name": expected_name,
            "data": {"color": "test color updated", "size": "test size updated"}}
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{new_object_id}',
        json=body, headers=headers)
    assert response.status_code == 200, f'Expected 200, got {response.status_code}'
    assert response.json()['name'] == expected_name, \
        f'Expected name {expected_name}, got {response.json()["name"]}'
    assert response.json()['data'] == body[
        'data'], f'Expected data {body["data"]}, got {response.json()["data"]}'
    response_no_name = requests.put(
        f'http://objapi.course.qa-practice.com/object/{new_object_id}',
        json={"data": body["data"]},
        headers=headers)
    assert response_no_name.status_code == 400, f'Expected 400, got {response_no_name.status_code}'
    response_no_data = requests.put(
        f'http://objapi.course.qa-practice.com/object/{new_object_id}',
        json={"name": body["name"]},
        headers=headers)
    assert response_no_data.status_code == 400, f'Expected 400, got {response_no_data.status_code}'


@allure.feature('Update data')
@allure.story('Update')
def test_verify_patch_object(new_object_id, inform_about_start_and_end_of_each_test):
    expected_name = "test updated 2"
    body = {"name": expected_name}
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{new_object_id}',
        json=body, headers=headers)
    assert response.status_code == 200, f'Expected 200, got {response.status_code}'
    assert response.json()['name'] == expected_name, \
        f'Expected name {expected_name}, got {response.json()["name"]}'
    assert response.json()['id'] == new_object_id, \
        f'Expected id {new_object_id}, got {response.json()["id"]}'


@allure.feature('Delete data')
@allure.story('Delete')
def test_verify_delete_object(new_object_id, inform_about_start_and_end_of_each_test):
    response = requests.delete(
        f'http://objapi.course.qa-practice.com/object/{new_object_id}')
    assert response.status_code == 200, f'Expected 200, got {response.status_code}'
    assert f'Object with id {new_object_id} successfully deleted' in response.text, \
        f'Expected deletion message, got {response.text}'
    response_not_found = requests.delete(
        'http://objapi.course.qa-practice.com/object/99999999999')
    assert response_not_found.status_code == 404, f'Expected 404, got {response_not_found.status_code}'

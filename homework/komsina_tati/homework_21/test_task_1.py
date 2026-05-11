import pytest
import requests
import allure

BASE_URL = 'http://objapi.course.qa-practice.com/object'
HEADERS = {'Content-Type': 'application/json'}


@allure.title('Получение объекта по id')
@allure.feature('Get data')
@allure.story('Get')
@pytest.mark.medium
def test_get_object_by_id(new_object_id, inform_about_start_and_end_testing,
                          inform_about_start_and_end_of_each_test):
    with allure.step(f'Отправить GET-запрос для объекта {new_object_id}'):
        response = requests.get(f'{BASE_URL}/{new_object_id}').json()

    with allure.step('Проверить, что id в ответе совпадает с запрошенным'):
        assert response['id'] == new_object_id


@allure.title('Создание нового объекта')
@allure.feature('Create data')
@allure.story('Post')
@pytest.mark.parametrize('expected_name',
                         ['expected_name_1', 'expected_name_2', 'expected_name_3'])
@pytest.mark.critical
def test_verify_post_new_object(new_object_id, expected_name,
                                inform_about_start_and_end_of_each_test):
    body = {"name": expected_name, "data": {"color": "test color", "size": "test size"}}

    with allure.step(f'Отправить POST-запрос с валидным телом (name={expected_name})'):
        response = requests.post(BASE_URL, json=body, headers=HEADERS)

    with allure.step('Проверить статус 200 и корректное имя в ответе'):
        assert response.status_code == 200, f'Expected 200, got {response.status_code}'
        assert response.json()['name'] == expected_name, \
            f'Expected {expected_name}, got {response.json()["name"]}'

    with allure.step('Отправить POST без поля name — ожидаем 400'):
        response_no_name = requests.post(BASE_URL, json={"data": body["data"]}, headers=HEADERS)
        assert response_no_name.status_code == 400, \
            f'Expected 400, got {response_no_name.status_code}'

    with allure.step('Отправить POST без поля data — ожидаем 400'):
        response_no_data = requests.post(BASE_URL, json={"name": body["name"]}, headers=HEADERS)
        assert response_no_data.status_code == 400, \
            f'Expected 400, got {response_no_data.status_code}'


@allure.title('Полное обновление объекта (PUT)')
@allure.feature('Update data')
@allure.story('Update')
def test_verify_put_object(new_object_id, inform_about_start_and_end_of_each_test):
    body = {"name": "test updated",
            "data": {"color": "test color updated", "size": "test size updated"}}

    with allure.step(f'Отправить PUT-запрос для объекта {new_object_id}'):
        response = requests.put(f'{BASE_URL}/{new_object_id}', json=body, headers=HEADERS)

    with allure.step('Проверить статус 200, имя и data в ответе'):
        assert response.status_code == 200, f'Expected 200, got {response.status_code}'
        assert response.json()['name'] == body['name'], \
            f'Expected {body["name"]}, got {response.json()["name"]}'
        assert response.json()['data'] == body['data'], \
            f'Expected {body["data"]}, got {response.json()["data"]}'

    with allure.step('Отправить PUT без поля name — ожидаем 400'):
        response_no_name = requests.put(f'{BASE_URL}/{new_object_id}',
                                        json={"data": body["data"]}, headers=HEADERS)
        assert response_no_name.status_code == 400, \
            f'Expected 400, got {response_no_name.status_code}'

    with allure.step('Отправить PUT без поля data — ожидаем 400'):
        response_no_data = requests.put(f'{BASE_URL}/{new_object_id}',
                                        json={"name": body["name"]}, headers=HEADERS)
        assert response_no_data.status_code == 400, \
            f'Expected 400, got {response_no_data.status_code}'


@allure.title('Частичное обновление объекта (PATCH)')
@allure.feature('Update data')
@allure.story('Update')
def test_verify_patch_object(new_object_id, inform_about_start_and_end_of_each_test):
    body = {"name": "test updated 2"}

    with allure.step(f'Отправить PATCH-запрос для объекта {new_object_id}'):
        response = requests.patch(f'{BASE_URL}/{new_object_id}', json=body, headers=HEADERS)

    with allure.step('Проверить статус 200, имя и id в ответе'):
        assert response.status_code == 200, f'Expected 200, got {response.status_code}'
        assert response.json()['name'] == body['name'], \
            f'Expected {body["name"]}, got {response.json()["name"]}'
        assert response.json()['id'] == new_object_id, \
            f'Expected id {new_object_id}, got {response.json()["id"]}'


@allure.title('Удаление объекта')
@allure.feature('Delete data')
@allure.story('Delete')
def test_verify_delete_object(new_object_id, inform_about_start_and_end_of_each_test):
    with allure.step(f'Отправить DELETE-запрос для объекта {new_object_id}'):
        response = requests.delete(f'{BASE_URL}/{new_object_id}')

    with allure.step('Проверить статус 200 и сообщение об удалении'):
        assert response.status_code == 200, f'Expected 200, got {response.status_code}'
        assert f'Object with id {new_object_id} successfully deleted' in response.text, \
            f'Expected deletion message, got {response.text}'

    with allure.step('Отправить DELETE для несуществующего объекта — ожидаем 404'):
        response_not_found = requests.delete(f'{BASE_URL}/99999999999')
        assert response_not_found.status_code == 404, \
            f'Expected 404, got {response_not_found.status_code}'

import pytest
import allure
from endpoint.post_object import PostObject
from endpoint.delete_object import DeleteObject

post_object = PostObject()
delete_object = DeleteObject()


@allure.feature('Object API')
@allure.story('POST')
class TestCreateObject:

    @allure.title('Создание объекта с валидными данными возвращает статус 200')
    @pytest.mark.critical
    @pytest.mark.parametrize('name', ['object_one', 'object_two', 'object_three'])
    def test_create_object_with_valid_data_returns_status_200(self, name):
        with allure.step(f'Отправить POST-запрос с name="{name}"'):
            response = post_object.create_object(name=name, color='red', size='large')

        with allure.step('Проверить, что статус ответа равен 200'):
            assert response.status_code == 200

        with allure.step('Удалить созданный объект (очистка после теста)'):
            delete_object.delete_object(response.json()['id'])

    @allure.title('Созданный объект содержит корректное имя в ответе')
    @pytest.mark.critical
    @pytest.mark.parametrize('name', ['object_one', 'object_two', 'object_three'])
    def test_create_object_response_contains_correct_name(self, name):
        with allure.step(f'Отправить POST-запрос с name="{name}"'):
            response = post_object.create_object(name=name, color='red', size='large')

        with allure.step(f'Проверить, что name в ответе равен "{name}"'):
            assert response.json()['name'] == name

        with allure.step('Удалить созданный объект (очистка после теста)'):
            delete_object.delete_object(response.json()['id'])

    @allure.title('Создание объекта без поля name возвращает статус 400')
    @pytest.mark.critical
    def test_create_object_without_name_returns_status_400(self):
        with allure.step('Отправить POST-запрос без поля name'):
            response = post_object.create_object_without_name(color='red', size='large')

        with allure.step('Проверить, что статус ответа равен 400'):
            assert response.status_code == 400

    @allure.title('Создание объекта без поля data возвращает статус 400')
    @pytest.mark.critical
    def test_create_object_without_data_returns_status_400(self):
        with allure.step('Отправить POST-запрос без поля data'):
            response = post_object.create_object_without_data(name='test object')

        with allure.step('Проверить, что статус ответа равен 400'):
            assert response.status_code == 400

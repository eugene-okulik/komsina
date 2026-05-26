import pytest
import allure
from endpoint.get_object import GetObject

get_object = GetObject()


@allure.feature('Object API')
@allure.story('GET')
class TestGetObject:

    @allure.title('Получение существующего объекта по id возвращает статус 200')
    @pytest.mark.medium
    def test_get_existing_object_returns_status_200(self, existing_object):
        object_id = existing_object['id']

        with allure.step(f'Отправить GET-запрос для объекта с id={object_id}'):
            response = get_object.get_object_by_id(object_id)

        with allure.step('Проверить, что статус ответа равен 200'):
            assert response.status_code == 200

    @allure.title('Получение существующего объекта по id возвращает корректный id')
    @pytest.mark.medium
    def test_get_existing_object_returns_correct_id(self, existing_object):
        object_id = existing_object['id']

        with allure.step(f'Отправить GET-запрос для объекта с id={object_id}'):
            response = get_object.get_object_by_id(object_id)

        with allure.step('Проверить, что id в ответе совпадает с запрошенным'):
            assert response.json()['id'] == object_id

    @allure.title('Получение несуществующего объекта возвращает статус 404')
    @pytest.mark.medium
    def test_get_non_existing_object_returns_status_404(self):
        non_existing_id = '99999999999'

        with allure.step(f'Отправить GET-запрос для несуществующего объекта id={non_existing_id}'):
            response = get_object.get_object_by_id(non_existing_id)

        with allure.step('Проверить, что статус ответа равен 404'):
            assert response.status_code == 404

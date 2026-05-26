import pytest
import allure
from endpoint.put_object import PutObject

put_object = PutObject()


@allure.feature('Object API')
@allure.story('PUT')
class TestUpdateObject:

    @allure.title('Полное обновление объекта возвращает статус 200')
    @pytest.mark.medium
    def test_update_object_returns_status_200(self, existing_object):
        object_id = existing_object['id']

        with allure.step(f'Отправить PUT-запрос для объекта с id={object_id}'):
            response = put_object.update_object(
                object_id=object_id,
                name='updated name',
                color='updated color',
                size='updated size'
            )

        with allure.step('Проверить, что статус ответа равен 200'):
            assert response.status_code == 200

    @allure.title('После полного обновления объект содержит новое имя')
    @pytest.mark.medium
    def test_update_object_response_contains_new_name(self, existing_object):
        object_id = existing_object['id']
        new_name = 'updated name'

        with allure.step(f'Отправить PUT-запрос с новым name="{new_name}"'):
            response = put_object.update_object(
                object_id=object_id,
                name=new_name,
                color='updated color',
                size='updated size'
            )

        with allure.step(f'Проверить, что name в ответе равен "{new_name}"'):
            assert response.json()['name'] == new_name

    @allure.title('После полного обновления объект содержит новые данные data')
    @pytest.mark.medium
    def test_update_object_response_contains_new_data(self, existing_object):
        object_id = existing_object['id']
        new_color = 'updated color'
        new_size = 'updated size'

        with allure.step(f'Отправить PUT-запрос с новыми color="{new_color}", size="{new_size}"'):
            response = put_object.update_object(
                object_id=object_id,
                name='updated name',
                color=new_color,
                size=new_size
            )

        with allure.step('Проверить, что data в ответе содержит обновлённые значения'):
            assert response.json()['data']['color'] == new_color
            assert response.json()['data']['size'] == new_size

    @allure.title('Полное обновление объекта без поля name возвращает статус 400')
    @pytest.mark.medium
    def test_update_object_without_name_returns_status_400(self, existing_object):
        object_id = existing_object['id']

        with allure.step(f'Отправить PUT-запрос без поля name для объекта id={object_id}'):
            response = put_object.update_object_without_name(
                object_id=object_id,
                color='some color',
                size='some size'
            )

        with allure.step('Проверить, что статус ответа равен 400'):
            assert response.status_code == 400

    @allure.title('Полное обновление объекта без поля data возвращает статус 400')
    @pytest.mark.medium
    def test_update_object_without_data_returns_status_400(self, existing_object):
        object_id = existing_object['id']

        with allure.step(f'Отправить PUT-запрос без поля data для объекта id={object_id}'):
            response = put_object.update_object_without_data(
                object_id=object_id,
                name='some name'
            )

        with allure.step('Проверить, что статус ответа равен 400'):
            assert response.status_code == 400

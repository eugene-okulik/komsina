import pytest
import allure
from endpoint.patch_object import PatchObject

patch_object = PatchObject()


@allure.feature('Object API')
@allure.story('PATCH')
class TestPartialUpdateObject:

    @allure.title('Частичное обновление объекта возвращает статус 200')
    @pytest.mark.medium
    def test_partial_update_object_returns_status_200(self, existing_object):
        object_id = existing_object['id']

        with allure.step(f'Отправить PATCH-запрос для объекта с id={object_id}'):
            response = patch_object.partial_update_object(
                object_id=object_id,
                name='partially updated name'
            )

        with allure.step('Проверить, что статус ответа равен 200'):
            assert response.status_code == 200

    @allure.title('После частичного обновления объект содержит новое имя')
    @pytest.mark.medium
    def test_partial_update_object_response_contains_new_name(self, existing_object):
        object_id = existing_object['id']
        new_name = 'partially updated name'

        with allure.step(f'Отправить PATCH-запрос с новым name="{new_name}"'):
            response = patch_object.partial_update_object(
                object_id=object_id,
                name=new_name
            )

        with allure.step(f'Проверить, что name в ответе равен "{new_name}"'):
            assert response.json()['name'] == new_name

    @allure.title('После частичного обновления id объекта остаётся прежним')
    @pytest.mark.medium
    def test_partial_update_object_id_remains_unchanged(self, existing_object):
        object_id = existing_object['id']

        with allure.step(f'Отправить PATCH-запрос для объекта с id={object_id}'):
            response = patch_object.partial_update_object(
                object_id=object_id,
                name='partially updated name'
            )

        with allure.step('Проверить, что id объекта не изменился'):
            assert response.json()['id'] == object_id

    @allure.title('После частичного обновления поле data остаётся неизменным')
    @pytest.mark.medium
    def test_partial_update_object_data_remains_unchanged(self, existing_object):
        object_id = existing_object['id']
        original_data = existing_object['data']

        with allure.step(f'Отправить PATCH-запрос — обновить только имя объекта'):
            response = patch_object.partial_update_object(
                object_id=object_id,
                name='partially updated name'
            )

        with allure.step('Проверить, что поле data не изменилось'):
            assert response.json()['data'] == original_data

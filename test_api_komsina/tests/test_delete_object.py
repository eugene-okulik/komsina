import pytest
import allure
from endpoint.delete_object import DeleteObject
from endpoint.get_object import GetObject

delete_object = DeleteObject()
get_object = GetObject()


@allure.feature('Object API')
@allure.story('DELETE')
class TestDeleteObject:

    @allure.title('Удаление существующего объекта возвращает статус 200')
    @pytest.mark.critical
    def test_delete_existing_object_returns_status_200(self, existing_object):
        object_id = existing_object['id']

        with allure.step(f'Отправить DELETE-запрос для объекта с id={object_id}'):
            response = delete_object.delete_object(object_id)

        with allure.step('Проверить, что статус ответа равен 200'):
            assert response.status_code == 200

    @allure.title('Ответ при удалении содержит сообщение об успешном удалении')
    @pytest.mark.critical
    def test_delete_existing_object_response_contains_success_message(self, existing_object):
        object_id = existing_object['id']

        with allure.step(f'Отправить DELETE-запрос для объекта с id={object_id}'):
            response = delete_object.delete_object(object_id)

        with allure.step('Проверить, что ответ содержит сообщение об удалении'):
            assert f'Object with id {object_id} successfully deleted' in response.text

    @allure.title('После удаления объект недоступен — GET возвращает статус 404')
    @pytest.mark.critical
    def test_deleted_object_is_not_accessible_anymore(self, existing_object):
        object_id = existing_object['id']

        with allure.step(f'Удалить объект с id={object_id}'):
            delete_object.delete_object(object_id)

        with allure.step('Отправить GET-запрос для удалённого объекта'):
            response = get_object.get_object_by_id(object_id)

        with allure.step('Проверить, что статус ответа равен 404'):
            assert response.status_code == 404

    @allure.title('Удаление несуществующего объекта возвращает статус 404')
    @pytest.mark.medium
    def test_delete_non_existing_object_returns_status_404(self):
        non_existing_id = '99999999999'

        with allure.step(f'Отправить DELETE-запрос для несуществующего объекта id={non_existing_id}'):
            response = delete_object.delete_object(non_existing_id)

        with allure.step('Проверить, что статус ответа равен 404'):
            assert response.status_code == 404

import pytest
import allure


@allure.feature('Object API')
@allure.story('DELETE')
class TestDeleteObject:

    @allure.title('Ответ при удалении содержит сообщение об успешном удалении')
    @pytest.mark.critical
    def test_delete_existing_object_response_contains_success_message(
            self, existing_object, delete_object):
        object_id = existing_object['id']

        with allure.step(f'Отправить DELETE-запрос для объекта с id={object_id}'):
            delete_object.delete_object(object_id)

        delete_object.check_status_is_200()

        with allure.step('Проверить, что ответ содержит сообщение об удалении'):
            assert f'Object with id {object_id} successfully deleted' in \
                   delete_object.response.text

    @allure.title('После удаления объект недоступен — GET возвращает статус 404')
    @pytest.mark.critical
    def test_deleted_object_is_not_accessible_anymore(
            self, existing_object, delete_object, get_object):
        object_id = existing_object['id']

        with allure.step(f'Удалить объект с id={object_id}'):
            delete_object.delete_object(object_id)

        with allure.step('Отправить GET-запрос для удалённого объекта'):
            get_object.get_object_by_id(object_id)

        get_object.check_status_is_404()

    @allure.title('Удаление несуществующего объекта возвращает статус 404')
    @pytest.mark.medium
    def test_delete_non_existing_object_returns_status_404(self, delete_object):
        with allure.step('Отправить DELETE-запрос для несуществующего объекта'):
            delete_object.delete_object('99999999999')

        delete_object.check_status_is_404()

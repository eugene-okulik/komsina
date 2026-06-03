import pytest
import allure


@allure.feature('Object API')
@allure.story('PATCH')
class TestPartialUpdateObject:

    @allure.title('После частичного обновления объект содержит новое имя')
    @pytest.mark.medium
    def test_partial_update_object_response_contains_new_name(
            self, existing_object, patch_object):
        object_id = existing_object['id']
        original_data = existing_object['data']
        body = {'name': 'partially updated name'}

        with allure.step(f'Отправить PATCH-запрос для объекта с id={object_id}'):
            patch_object.partial_update_object(object_id, body)

        patch_object.check_status_is_200()
        patch_object.check_response_name_is_correct(body['name'])
        patch_object.check_response_data_is_correct(original_data)

    @allure.title('После частичного обновления id объекта остаётся неизменным')
    @pytest.mark.medium
    def test_partial_update_object_id_remains_unchanged(
            self, existing_object, patch_object):
        object_id = existing_object['id']
        body = {'name': 'partially updated name'}

        with allure.step('Отправить PATCH-запрос — обновить только имя объекта'):
            patch_object.partial_update_object(object_id, body)

        patch_object.check_status_is_200()

        with allure.step('Проверить, что id объекта не изменился'):
            assert patch_object.json['id'] == object_id

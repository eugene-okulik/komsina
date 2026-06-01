import pytest
import allure


@allure.feature('Object API')
@allure.story('PUT')
class TestUpdateObject:

    @allure.title('После полного обновления объект содержит новое имя и данные')
    @pytest.mark.medium
    def test_update_object_response_contains_new_data(self, existing_object, put_object):
        object_id = existing_object['id']
        body = {
            'name': 'updated name',
            'data': {'color': 'updated color', 'size': 'updated size'}
        }

        with allure.step(f'Отправить PUT-запрос для объекта с id={object_id}'):
            put_object.update_object(object_id, body)

        put_object.check_status_is_200()
        put_object.check_response_name_is_correct(body['name'])

        with allure.step('Проверить, что data в ответе содержит обновлённые значения'):
            assert put_object.json['data'] == body['data']

    @allure.title('Полное обновление без обязательных полей возвращает статус 400')
    @pytest.mark.medium
    @pytest.mark.parametrize('body', [
        {'data': {'color': 'some color', 'size': 'some size'}},
        {'name': 'some name'}
    ])
    def test_update_object_without_required_fields_returns_status_400(
            self, body, existing_object, put_object):
        with allure.step(f'Отправить PUT-запрос с телом: {body}'):
            put_object.update_object(existing_object['id'], body)

        put_object.check_status_is_400()

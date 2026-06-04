import pytest
import allure
from test_data import DEFAULT_COLOR, DEFAULT_SIZE


@allure.feature('Object API')
@allure.story('POST')
class TestCreateObject:

    @allure.title('Созданный объект содержит корректное имя в ответе')
    @pytest.mark.critical
    @pytest.mark.parametrize('name', ['object_one', 'object_two', 'object_three'])
    def test_create_object_response_contains_correct_name(
            self, name, post_object, delete_object):
        body = {'name': name, 'data': {'color': DEFAULT_COLOR, 'size': DEFAULT_SIZE}}

        with allure.step(f'Отправить POST-запрос с name="{name}"'):
            post_object.create_object(body)

        post_object.check_status_is_200()
        post_object.check_response_name_is_correct(name)

        with allure.step('Удалить созданный объект (очистка после теста)'):
            delete_object.delete_object(post_object.json['id'])

    @allure.title('Создание объекта без обязательных полей возвращает статус 400')
    @pytest.mark.critical
    @pytest.mark.parametrize('body', [
        {'data': {'color': DEFAULT_COLOR, 'size': DEFAULT_SIZE}},
        {'name': 'test object'}
    ])
    def test_create_object_without_required_fields_returns_status_400(
            self, body, post_object):
        with allure.step(f'Отправить POST-запрос с телом: {body}'):
            post_object.create_object(body)

        post_object.check_status_is_400()

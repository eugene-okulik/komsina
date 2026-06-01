import pytest
import allure


@allure.feature('Object API')
@allure.story('GET')
class TestGetObject:

    @allure.title('Получение существующего объекта по id возвращает корректный id')
    @pytest.mark.medium
    def test_get_existing_object_returns_correct_id(self, existing_object, get_object):
        object_id = existing_object['id']

        with allure.step(f'Отправить GET-запрос для объекта с id={object_id}'):
            get_object.get_object_by_id(object_id)

        get_object.check_status_is_200()
        get_object.check_response_name_is_correct(existing_object['name'])

    @allure.title('Получение несуществующего объекта возвращает статус 404')
    @pytest.mark.medium
    def test_get_non_existing_object_returns_status_404(self, get_object):
        with allure.step('Отправить GET-запрос для несуществующего объекта'):
            get_object.get_object_by_id('99999999999')

        get_object.check_status_is_404()

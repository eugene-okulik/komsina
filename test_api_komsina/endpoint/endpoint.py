import allure


class Endpoint:
    url = 'http://objapi.course.qa-practice.com/object'
    response = None
    json = None
    headers = {'Content-Type': 'application/json'}

    @allure.step('Проверить, что статус ответа равен 200')
    def check_status_is_200(self):
        assert self.response.status_code == 200, (
            f'Ожидался статус 200, получен {self.response.status_code}'
        )

    @allure.step('Проверить, что статус ответа равен 400')
    def check_status_is_400(self):
        assert self.response.status_code == 400, (
            f'Ожидался статус 400, получен {self.response.status_code}'
        )

    @allure.step('Проверить, что статус ответа равен 404')
    def check_status_is_404(self):
        assert self.response.status_code == 404, (
            f'Ожидался статус 404, получен {self.response.status_code}'
        )

    @allure.step('Проверить, что name в ответе корректный')
    def check_response_name_is_correct(self, name):
        assert self.json['name'] == name, (
            f'Ожидалось имя "{name}", получено "{self.json["name"]}"'
        )

    @allure.step('Проверить, что data в ответе корректная')
    def check_response_data_is_correct(self, data):
        assert self.json['data'] == data, (
            f'Ожидалась data "{data}", получена "{self.json["data"]}"'
        )

    @allure.step('Проверить, что объект успешно удалён')
    def check_deletion_message(self, object_id):
        assert f'Object with id {object_id} successfully deleted' in self.response.text, (
            f'Ожидалось сообщение об удалении объекта {object_id}'
        )

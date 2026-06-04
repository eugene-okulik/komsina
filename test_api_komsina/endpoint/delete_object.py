import allure
import requests
from .endpoint import Endpoint


class DeleteObject(Endpoint):

    @allure.step('Отправить DELETE-запрос для удаления объекта')
    def delete_object(self, object_id):
        self.response = requests.delete(
            f'{self.url}/{object_id}', headers=self.headers
        )
        return self.response

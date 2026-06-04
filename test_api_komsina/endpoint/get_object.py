import allure
import requests
from .endpoint import Endpoint


class GetObject(Endpoint):

    @allure.step('Отправить GET-запрос для объекта')
    def get_object_by_id(self, object_id):
        self.response = requests.get(
            f'{self.url}/{object_id}', headers=self.headers
        )
        if self.response.ok:
            self.json = self.response.json()
        return self.response

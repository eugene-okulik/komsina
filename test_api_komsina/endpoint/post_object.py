import allure
import requests
from .endpoint import Endpoint


class PostObject(Endpoint):

    @allure.step('Отправить POST-запрос для создания объекта')
    def create_object(self, body):
        self.response = requests.post(
            self.url, json=body, headers=self.headers
        )
        if self.response.ok:
            self.json = self.response.json()
        return self.response

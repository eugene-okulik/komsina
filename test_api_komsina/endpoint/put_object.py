import allure
import requests
from .endpoint import Endpoint


class PutObject(Endpoint):

    @allure.step('Отправить PUT-запрос для обновления объекта')
    def update_object(self, object_id, body):
        self.response = requests.put(
            f'{self.url}/{object_id}', json=body, headers=self.headers
        )
        if self.response.ok:
            self.json = self.response.json()
        return self.response

import allure
import requests
from .endpoint import Endpoint


class PatchObject(Endpoint):

    @allure.step('Отправить PATCH-запрос для частичного обновления объекта')
    def partial_update_object(self, object_id, body):
        self.response = requests.patch(
            f'{self.url}/{object_id}', json=body, headers=self.headers
        )
        if self.response.ok:
            self.json = self.response.json()
        return self.response

from locust import HttpUser, task
import random


class ObjectApiUser(HttpUser):

    def on_start(self):
        self.object_ids = []
        body = {
            'name': 'locust test object',
            'data': {
                'color': 'test color',
                'size': 'test size'
            }
        }
        response = self.client.post('/object', json=body)
        self.object_ids.append(response.json()['id'])

    def on_stop(self):
        for object_id in self.object_ids:
            self.client.delete(f'/object/{object_id}')

    @task(3)
    def get_object(self):
        self.client.get(f'/object/{random.choice(self.object_ids)}')

    @task(1)
    def create_and_delete_object(self):
        body = {
            'name': 'locust temp object',
            'data': {
                'color': 'temp color',
                'size': 'temp size'
            }
        }
        response = self.client.post('/object', json=body)
        if response.ok:
            object_id = response.json()['id']
            self.client.delete(f'/object/{object_id}')
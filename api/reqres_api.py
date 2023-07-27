import requests


class ReqresAPI:
    def __init__(self, host, json=None, params=None):
        self.host = host
        self.headers = None

    def list_users(self, path='/api/users', params=None):
        return requests.get(self.host + path, params=params, headers=self.headers)

    def fetches_user(self, path='/api/users/{user_id}', user_id=''):
        return requests.get(self.host + path.format(user_id=user_id))

    def list_resources(self, path='/api/unknown', params=None):
        return requests.get(self.host + path, params=params, headers=self.headers)

    def fetches_resource(self, path='/api/unknown/{resource_id}', resource_id=''):
        return requests.get(self.host + path.format(resource_id=resource_id), headers=self.headers)

    def create_user(self, path='/api/users', json=None):
        return requests.post(self.host + path, json=json)

    def update_user_method_put(self, path='/api/users/{user_id}', user_id='', json=None):
        return requests.put(self.host + path.format(user_id=user_id), json=json)

    def update_user_method_patch(self, path='/api/users/{user_id}', user_id='', json=None):
        return requests.patch(self.host + path.format(user_id=user_id), json=json)

    def delete_user(self, path='/api/users/{user_id}', user_id=''):
        return requests.delete(self.host + path.format(user_id=user_id))

    def register(self, path='/api/register', json=None):
        return requests.post(self.host + path, json=json)

    def login(self, path='/api/login', json=None):
        return requests.post(self.host + path, json=json)

import requests


class ReqresAPI:
    def __init__(self, host, json=None, params=None):
        self.host = host
        self.headers = None

    def list_users(self, path='/api/users', params=None):
        return requests.get(self.host + path, params=params, headers=self.headers)

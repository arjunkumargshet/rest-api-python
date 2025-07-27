
import requests

class UserAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def create_user(self, payload):
        return requests.post(f"{self.base_url}/users", json=payload)

    def get_user(self, user_id):
        return requests.get(f"{self.base_url}/users/{user_id}")

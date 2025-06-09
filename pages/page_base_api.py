import pytest
from playwright.sync_api import Page
import requests


class BaseApi:
    BASE_URL="https://jsonplaceholder.typicode.com"


class UserApi(BaseApi):
    def get_users(self):
        """Получить список всех пользователей."""
        url = f"{self.BASE_URL}/users"
        return requests.get(url)

    def get_user(self, user_id):
        """Получить одного пользователя по ID."""
        url = f"{self.BASE_URL}/users/{user_id}"  # исправь на /users/{user_id}
        return requests.get(url)


class PostApi(BaseApi):
    def get_posts(self, user_id=None):
        url = f"{self.BASE_URL}/posts"
        params = {"userId": user_id} if user_id is not None else {}
        return requests.get(url, params=params)

# создать новый пост (словарь post_data)
    def create_posts(self, post_data):
        url = f"{self.BASE_URL}/posts"
        return requests.post(url, json=post_data)

class CommentsApi(BaseApi):
    def get_comments(self):
        url = f"{self.BASE_URL}/comments"
        return requests.get(url)
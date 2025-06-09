from pages.page_base_api import BaseApi

from pages.page_base_api import PostApi  # Импортируем правильный класс

def test_create_post():
    api = PostApi()  # ✅ Используем PostApi вместо BaseApi
    new_post = {
        "title": "Test Post",
        "body": "Content of the test post",
        "userId": 1
    }
    response = api.create_posts(new_post)  # ✅ Вызов правильного метода
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Post"
    assert data["body"] == "Content of the test post"
    assert data["userId"] == 1
    assert "id" in data
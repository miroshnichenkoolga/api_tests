import pytest
from pages.page_base_api import PostApi

@pytest.mark.parametrize("user_id", [1, 2, 3, 10])
def test_get_posts_by_user(user_id):
    api = PostApi()
    response = api.get_posts(user_id=user_id)
    assert response.status_code == 200

    posts = response.json()
    assert isinstance(posts, list)

    for post in posts:
        assert post["userId"] == user_id, f"Expected userId={user_id}, got {post['userId']}"
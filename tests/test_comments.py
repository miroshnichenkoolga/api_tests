import requests

from pages.page_base_api import BaseApi, CommentsApi, UserApi


def test_comments_list():
    api= CommentsApi()
    response = api.get_comments()
    assert response.status_code == 200

    data = response.json()
    print(f"Первый коммент: {data[0]}")
    assert isinstance(data, list)
    assert len(data) >0
    assert "postId" in data[0]

def test_comments_not_found():
    api=CommentsApi()
    non_exist_id = 9877777
    url = f"{api.BASE_URL}/posts/{non_exist_id}"
    response = requests.get(url)
    assert response.status_code == 404
    print(f"Status code for non-existing ID: {response.status_code}")
from pages.page_base_api import BaseApi, UserApi


def test_list_users():
    api = UserApi()
    response = api.get_users()
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    first_user = data[0]
    assert "id" in first_user
    assert "email" in first_user
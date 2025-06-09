from pages.page_base_api import UserApi

def test_get_single_user():
    api = UserApi()
    user_id = 1
    response = api.get_user(user_id)
    print(f"Status Code: {response.status_code}")
    assert response.status_code == 200
    user_data = response.json()
    assert user_data["id"] == 1
    assert user_data["username"]
    assert "@" in user_data["email"]



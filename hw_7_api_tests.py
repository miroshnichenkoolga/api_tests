import data as data
import requests
import requests
import data as data
import json
# запрос других ресурсов
url_get = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url_get)
# Выводим код ответа и некоторые заголовки, чтобы убедиться, что запрос успешен
print("Status Code:", response.status_code)
print("Content-Type:", response.headers.get("Content-Type"))  # Тип данных (JSON)

assert response.status_code==200

data = response.json()
assert data[0]["email"] == "Sincere@april.biz"
assert data[1]["name"] == "Ervin Howell"

# создание нового
url_post = "https://jsonplaceholder.typicode.com/comments"
payload = {
    "postId": 76,
    "id": 345,
    "name": "Olga",
    "email": "Donll@polly.net",
    "body": "sequi76"
}
response_post = requests.post(url_post, json=payload)

print("Status Code:", response_post.status_code)
print("Response JSON (POST):", response_post.json())
print("Content-Type:", response_post.headers.get("Content-Type"))

assert response_post.status_code == 201
assert response_post.json()["name"] =="Olga"
assert response_post.json()["email"] == "Donll@polly.net"

# невалидный джейсон
invalid_url = "https://jsonplaceholder.typicode.com/posts/9999"
response_invalid_url = requests.get(invalid_url)

print("Status Code:", response_invalid_url.status_code)
print("Response JSON (invalid url):", response_invalid_url.json())
assert response_invalid_url.status_code == 404
assert response_invalid_url.json() =={}
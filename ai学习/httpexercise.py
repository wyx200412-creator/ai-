
import requests

params = {
    "userId": 1
}

response = requests.get(
    "https://jsonplaceholder.typicode.com/todos",
    params=params
)

print(response.url)

new_task = {
    "userId": 1,
    "title": "学习 HTTP",
    "completed": False
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/xxxx",
    json=new_task
)

response.raise_for_status()
data = response.json()

print(data)
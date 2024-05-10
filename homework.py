import requests
from pprint import pprint


print(f"{'-' * 50} Задание 1: Получение данных {'-' * 50}")

url = "https://api.github.com/search/repositories"
params = {"q": "html"}
try:
    response = requests.get(url, params=params)
except Exception as e:
    print(f"Произошла ошибка: {e}")
else:
    print(f"---- Статус-код ответа: {response.status_code}")
    response_json = response.json()
    print(f"---- Количество репозиториев HTML: {response_json['total_count']}")
    print("---- Полученные данные:")
    pprint(response.json())
print()

# ---------------------------------------------------------------
print(f"{'-' * 50} Задание 2: Параметры запроса {'-' * 50}")

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "Тестовый POST-запрос",
    "body": "Тестовый контент POST-запроса",
    "userId": 1
}
try:
    response = requests.get(url, data=data)
except Exception as e:
    print(f"Произошла ошибка: {e}")
else:
    print(f"---- Статус-код ответа: {response.status_code}")
    print("---- Полученные данные:")
    pprint(response.json())
print()

# ---------------------------------------------------------------
print(f"{'-' * 50} Задание 3: Отправка данных {'-' * 50}")

url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "Тестовый POST-запрос Задания 3",
    "body": "Тестовый контент POST-запроса Задания 3",
    "userId": 1
}

try:
    response = requests.post(url, data=data)
except Exception as e:
    print(f"Произошла ошибка: {e}")
else:
    print(f"---- Статус-код ответа: {response.status_code}")
    print("---- Полученные данные:")
    pprint(response.json())

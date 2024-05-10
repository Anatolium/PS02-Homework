import requests
import pprint

# response = requests.get("https://www.google.com")
# if response.ok:
#     print ("Запрос успешно выполнен")
# else:
#     print ("Произошла ошибка")
# print(response.status_code)
# print(response.headers)
# response.text – "тело" ответа, это и есть код html данной страницы
# print (response.text)
# # То же, что 'print (response.text)', но в одну строчку:
# print (response.content)

# response = requests.get("https://api.github.com")
# print(response.text)
# response_json = response.json()
# pprint.pprint(response_json)

# params = {"q": "python"}
# response = requests.get("https://api.github.com/search/repositories", params=params)
# response_json = response.json()
# print(f"Количество репозиториев Python: {response_json['total_count']}")
# Тот же запрос в строке браузера "https://api.github.com/search/repositories?q=python"

# img = "https://img2.fonwall.ru/o/fx/kot-koshka-ryzhiy.jpg"
# response = requests.get(img)
#
# with open("picture.jpg", "wb") as file:
#     try:
#         file.write(response.content)
#     except Exception as e:
#         print(f"Произошла ошибка: {e}")
#     else:
#         print("Изображение по этому адресу получено")

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "Тестовый POST-запрос",
    "body": "Тестовый контент POST-запроса",
    "userId": 2
}
try:
    response = requests.post(url, data=data)
except Exception as e:
    print(f"Произошла ошибка: {e}")
else:
    print(response.status_code)
    print(f"{response.json()}")



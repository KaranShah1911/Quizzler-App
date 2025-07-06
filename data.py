import requests

parameters = {
    "amount": 10,
    "category": 22,
    "difficulty": "easy",
    "type": "boolean",
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
# print(response.status_code)
question_data = data['results']



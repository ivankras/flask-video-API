import requests

BASE = 'http://127.0.0.1:5000'

# response = requests.post(f'{BASE}/video/2', {'name': 'myvideo2', 'views': 929, 'likes': 210})
# print(response.json())

response = requests.patch(f'{BASE}/video/2', {'views': 930, 'likes': 209})
print(response.json())

response = requests.get(f'{BASE}/video/2')
print(response.json())

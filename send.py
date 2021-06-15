import requests

headers = {}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjIzMzE4MjMzLCJqdGkiOiJkMTBlNDlkM2RiZWU0NGZhOTc2Y2E0Y2JkZjllODExNCIsInVzZXJfaWQiOjF9.Kp1kdOvu7Jgcgf1rDrLvshhpKJe9YvFZXL8saHv8kjU'

r = requests.get('http://127.0.0.1:8000/paradigms' , headers=headers)

print(r.text)
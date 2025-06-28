# Interact with external services.
import requests
res = requests.get("https://api.github.com")
print(res.status_code)

data = res.json()
print(data['current_user_url'])

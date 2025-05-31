import requests
import json

url = 'https://pmsc.xuno.com.au/api/v1/index.php/students/46/timetable?date=2025-05-31&session_key=1JB2lOgWUqjPGlJYQudKcMqHMdQntYSm'

with open("cookies_secret.json", "r") as f:
    cookies = json.load(f)

cookie_header = "; ".join(
    f"{c['name']}={c['value']}"
    for c in cookies
    if c.get("path") == "/"
)
headers = {
    'Cookie': cookie_header,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    'Referer': 'https://pmsc.xuno.com.au/index.php/dashboard',
    'Accept': 'application/json, text/plain, */*',
}

response = requests.get(url, headers=headers)

with open("timetable.json", "w") as f:
    json.dump(response.json(), f)



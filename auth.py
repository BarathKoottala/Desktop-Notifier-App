import requests
import requests.auth

def get_auth():
    client_auth = requests.auth.HTTPBasicAuth('', '')
    post_data = {"grant_type": "password", "username": "", "password": ""}

    headers = {"User-Agent": "uplifting_news_notifier/0.1 by grahamaubrey"}
    response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
    print(response.json())

    json = response.json()

    access_token = json["access_token"]
    expiry_in_seconds = json["expires_in"]
    token_type = json["token_type"]

    return (access_token, expiry_in_seconds, token_type)

get_auth()
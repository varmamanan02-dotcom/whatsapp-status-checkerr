
import requests
import json

print("=== WhatsApp Display Name Checker ===")

token = input("Enter your Meta Access Token: ")

phone_id = "1391882410678040"

version = "vXX.X"

url = f"https://graph.facebook.com/{version}/{phone_id}"

params = {
    "fields": "display_phone_number,verified_name,name_status",
    "access_token": token
}

response = requests.get(url, params=params)

print("\nMeta API Response:")
print("HTTP Status:", response.status_code)
print(json.dumps(response.json(), indent=4))

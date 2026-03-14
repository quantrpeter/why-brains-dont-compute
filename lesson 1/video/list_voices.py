import requests
import json

api_key = "sk_6d0df3daa81d3602181933cded228b4071a5edb7a5f910f5"
url = "https://api.elevenlabs.io/v1/voices"
headers = {"xi-api-key": api_key}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    voices = response.json().get('voices', [])
    print(f"Found {len(voices)} voices:")
    for v in voices:
        print(f"- {v.get('name')} ({v.get('voice_id')})")
        print(f"  Labels: {v.get('labels')}")
else:
    print(f"Error: {response.status_code}")

import requests

token = 'Qx8bePy2Hxre3Rj1VoyfmmKfl3gu71A5nHnfgeHz'
headers = {
        'Authorization': f'Bearer {token}'
    }
url = 'https://api.nasa.gov/planetary/apod'
response = requests.get(url, headers=headers)
response.raise_for_status()

print(response)
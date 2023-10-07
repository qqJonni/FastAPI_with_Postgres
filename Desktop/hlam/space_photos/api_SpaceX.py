import requests
import json


url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
response = requests.get(url)
response.raise_for_status()

data_json = json.loads(response.content)

original_links = data_json["links"]["flickr"]["original"]

print(original_links)
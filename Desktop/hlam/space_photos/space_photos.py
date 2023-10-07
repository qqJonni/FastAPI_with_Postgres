import os
import requests
import json


def upload_image(url, upload_to):
    filename = os.path.join(upload_to, f'spacex{url_number}.jpeg')
    url = url
    response = requests.get(url)
    response.raise_for_status()

    with open(filename, 'wb')as file:
        file.write(response.content)


url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
response = requests.get(url)
response.raise_for_status()

data_json = json.loads(response.content)

original_links = data_json["links"]["flickr"]["original"]

for url_number, url in enumerate(original_links):
    upload_image(url, 'images')

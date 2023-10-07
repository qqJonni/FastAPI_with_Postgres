import os
import requests
import json
from urllib.parse import urlparse


def upload_image(url, upload_to):
    filename = os.path.join(upload_to, 'hubble.jpeg')
    url = url
    response = requests.get(url)
    response.raise_for_status()

    with open(filename, 'wb')as file:
        file.write(response.content)


def fetch_spacex_last_launch(url, upload_to):
    url = url
    response = requests.get(url)
    response.raise_for_status()

    data_json = json.loads(response.content)

    original_links = data_json["links"]["flickr"]["original"]

    for url_number, url in enumerate(original_links):
        filename = os.path.join(upload_to, f'spacex{url_number}.jpeg')
        with open(filename, 'wb') as file:
            file.write(response.content)


def get_file_format(url):
    url = url

    res = os.path.splitext(url)
    file_format = urlparse(res[1])

    return file_format.path


fetch_spacex_last_launch('https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a', 'images')

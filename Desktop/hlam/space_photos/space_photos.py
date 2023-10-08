import os
import requests
import json
from urllib.parse import urlparse
from dotenv import load_dotenv, find_dotenv


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


def upload_apod_nasa_images(url, upload_to):
    load_dotenv(find_dotenv())
    token = os.environ.get('APOD_TOKEN')

    url = url
    response = requests.get(f'{url}?count=30&api_key={token}')
    response.raise_for_status()

    data_json = json.loads(response.content)

    original_links = [entry['hdurl'] for entry in data_json if 'hdurl' in entry]

    for url_number, url in enumerate(original_links):
        filename = os.path.join(upload_to, f'nasa_apod_{url_number}.jpeg')
        with open(filename, 'wb') as file:
            file.write(response.content)


def upload_epic_nasa_photo(url, upload_to):
    load_dotenv(find_dotenv())
    token = os.environ.get('APOD_TOKEN')

    url = f'{url}{token}'
    response = requests.get(url)
    data_json = json.loads(response.content)
    original_dates = [entry['date'] for entry in data_json if 'date' in entry]
    original_image = [entry['image'] for entry in data_json if 'image' in entry]

    original_links = []
    for date, image in zip(original_dates, original_image):
        year = date[0:4]
        month = date[5:7]
        day = date[8:10]
        image_url = f'https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{image}.png?api_key={token}'
        original_links.append(image_url)

    for url_number, url in enumerate(original_links):
        filename = os.path.join(upload_to, f'epic_photo_{url_number}.png')
        with open(filename, 'wb') as file:
            file.write(response.content)



import os
import requests


def upload_image(url, upload_to):
    filename = os.path.join(upload_to, 'hubble.jpeg')
    url = url
    response = requests.get(url)
    response.raise_for_status()

    with open(filename, 'wb')as file:
        file.write(response.content)


upload_image('https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg', 'images')

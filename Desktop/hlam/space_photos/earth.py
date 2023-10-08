import os
import json

import requests
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
token = os.environ.get('APOD_TOKEN')

url = f'https://api.nasa.gov/EPIC/api/natural/images?api_key={token}'
response = requests.get(url)
res = response.text.split(',')
data_json = json.loads(response.content)
original_dates = [entry['date'] for entry in data_json if 'date' in entry]
original_image = [entry['image'] for entry in data_json if 'image' in entry]
first_date = original_dates[0]
first_year = first_date[0:4]
first_month = first_date[5:7]
first_day = first_date[8:10]
first_image = original_image[0]

new_url = f'https://api.nasa.gov/EPIC/archive/natural/{first_year}/{first_month}/{first_day}/png/{first_image}.png?api_key={token}'
print(new_url)

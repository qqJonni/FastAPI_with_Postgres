import telegram
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
bot = telegram.Bot(os.environ.get('TELEGRAM_TOKEN'))

bot.send_photo('1500316931', open('/Users/valeriy/Downloads/photo-thumb-37546.png', 'rb'))


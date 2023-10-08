import telegram
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
bot = telegram.Bot(os.environ.get('TELEGRAM_TOKEN'))
print(bot.get_me())


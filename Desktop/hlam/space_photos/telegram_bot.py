import telegram
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
bot = telegram.Bot(os.environ.get('TELEGRAM_TOKEN'))

bot.send_message(chat_id='1500316931', text="I'm sorry Dave I'm afraid I can't do that.")


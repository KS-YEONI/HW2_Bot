import telegram
import schedule
import time
import pytz
import datetime
import asyncio


# Bot: K_2022_2_sy_bot
# channel = K2022test
# chat_id = "6775614712"
# token = 6419179666:AAHBYnaxOF5_DvVYCsE0RauGx6ZHIfCbY2Y

# function
def send_message():
    chat_id = "6775614712"
    bot_token = "6419179666:AAHBYnaxOF5_DvVYCsE0RauGx6ZHIfCbY2Y"
    bot = telegram.Bot(token=bot_token)

    now = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    if now.hour >= 23 or now.hour <= 6:
        return
    asyncio.run(bot.sendMessage(chat_id=chat_id, text = "알람"))

send_message()
schedule.every(1).minutes.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)

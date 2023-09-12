#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", 23313487, cast=int)
API_HASH = config("API_HASH", "6aa6136dd5028dad918b7a81a379fcb6")
BOT_TOKEN = config("BOT_TOKEN", "6394845891:AAHSoudKqIiCnW_9ZVw_fWdDxNYyC1qZ7Sk")
SESSION = config("SESSION", "1BJWap1sBu4RLJL8TaW03fpcIZba-xJUhRZ4ojBkuN-c7MLATr-QhtZT3pp9jtVOnkelFMrY3DKZQbKD_xdER6KjSmHMqdqhty0EM_JtsDjT5nW0fMLmZNp7mHjGknbV62iSKtBuEJxgc8i-ISO392Klj3WONeVN-8jJotImH8aO5wOadfuQTFgYkO20_1DZFGy5Dd-1Uo0l6jXuge5w-w_8VnoBT7LaK4wfa3U8HOY_LZ238-Y8KwEZiJaObjkTcrY8hrGj25Ja2PVEhqNHDWZvN0n9vpujEwEVAXpTP_a-k2tOy40tLbw91p0FAORDHSr1wbwlSRi0BKquNcYIHPK2e--RlLjI=")
FORCESUB = config("FORCESUB", "donbroo22222111109393388z")
AUTH = config("AUTH", 5607896636, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)

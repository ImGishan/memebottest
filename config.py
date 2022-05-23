from dotenv import load_dotenv
from os import environ
from pyrogram.types import ReplyKeyboardMarkup,InlineKeyboardMarkup, InlineKeyboardButton

load_dotenv("config.env")

BOT_OWNER = 1467358214
BOT_TOKEN = environ.get("BOT_TOKEN", None)
API_ID = int(environ.get("API_ID", 6))
API_HASH = environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
DATABASE = environ.get("DATABASE")
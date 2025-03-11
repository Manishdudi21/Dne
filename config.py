import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    AUTH_USER = os.environ.get('AUTH_USERS', '').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-five.vercel.app"
    CREDIT = "Iɴᴅɪᴀɴ ✗ Wᴀʀʀɪᴏʀꜱ" #Here You Can Change with Your Name  or any custom name or title you prefer
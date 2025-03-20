import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7878947785:AAGxCaq9vARiLMyJtKrWSms3_ThTa-bMBHc")
    API_ID = int(os.environ.get("API_ID", "20589413"))
    API_HASH = os.environ.get("API_HASH", "654d559a9a91daeecd9e760fc73e6766")
    AUTH_USER = os.environ.get('AUTH_USERS', '6631452970').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://uploader-drm-6a0cf44af499.herokuapp.com/"
    CREDIT = "sheffyssamra" #Here You Can Change with Your Name  or any custom name or title you prefer

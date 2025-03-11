import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7441315027:AAEfcoSuD_Cz7p_OoV0oVYe4-5irG5S6G2M")
    API_ID = int(os.environ.get("API_ID", "20589413"))
    API_HASH = os.environ.get("API_HASH", "654d559a9a91daeecd9e760fc73e6766")
    AUTH_USER = os.environ.get('AUTH_USERS', '6514361814').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://uploader-drm-6a0cf44af499.herokuapp.com/"
    CREDIT = "sheffyssamra" #Here You Can Change with Your Name  or any custom name or title you prefer

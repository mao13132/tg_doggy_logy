import os

from dotenv import load_dotenv

project_path = os.path.dirname(__file__)

dotenv_path = os.path.join(os.path.dirname(__file__), 'src', '.env')

load_dotenv(dotenv_path)

DEVELOPER = 1422194909

ADMIN = ['1422194909']

TOKEN = os.getenv('TOKEN')

START_MESSAGE = '🐱 Что бы начать анкетирование, пожалуйста, воспользуйтесь кнопкой ниже👇'

ADMIN_CHANEL = '-1001769946855'

LOGO = r'src/telegram/media/logo.jpg'  # путь аватарки

LOGGER = True

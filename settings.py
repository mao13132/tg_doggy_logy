import os

from dotenv import load_dotenv

project_path = os.path.dirname(__file__)

dotenv_path = os.path.join(os.path.dirname(__file__), 'src', '.env')

report_path = os.path.join(os.path.dirname(__file__), 'src', 'reports')

load_dotenv(dotenv_path)

DEVELOPER = 1422194909

ADMIN = ['1422194909', '1305714512']

TOKEN = os.getenv('TOKEN')

START_MESSAGE = '🐶 Что бы начать анкетирование, пожалуйста, воспользуйтесь кнопкой ниже👇'

END_MSG = f'✅Опрос закончен! Благодарим за ответы!'

ADMIN_CHANEL = '-1001769946855'

LOGO = r'src/telegram/media/logo.jpg'

IMG1 = r'src/telegram/media/1.jpg'
IMG2 = r'src/telegram/media/2.jpg'
IMG3 = r'src/telegram/media/3.jpg'
IMG4 = r'src/telegram/media/4.jpg'
IMG5 = r'src/telegram/media/5.jpg'
IMG6 = r'src/telegram/media/6.jpg'
IMG7 = r'src/telegram/media/7.jpg'
IMG8 = r'src/telegram/media/8.jpg'
IMG9 = r'src/telegram/media/9.jpg'

LOGGER = True

COUNT_QUEST_DATE = 7

import os

BOT_TOKEN = os.getenv('1565891278:AAFYvbj4dDy5UCZesONpdd5W4DJR6xpSIIk')
if not BOT_TOKEN:
    print('You have forgot to set BOT_TOKEN')
    quit()

HEROKU_APP_NAME = os.getenv('telegrambot22213131')


# webhook settings
WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{BOT_TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

# webserver settings
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = int(os.getenv('PORT')) 

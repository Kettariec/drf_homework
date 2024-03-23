import os
import requests
from django.core.management import BaseCommand


class Command(BaseCommand):
    URL = 'https://api.telegram.org/'
    Token = os.getenv('Telegram_Token')

    def handle(self, *args, **options):

        requests.post(url=f'{self.URL}bot{self.Token}/sendMessage',
                      data={'chat_id': '493656021',
                            'text': 'Вы подписались на курс!'
                            },)

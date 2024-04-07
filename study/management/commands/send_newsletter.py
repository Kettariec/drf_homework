import os
import requests
from django.core.management import BaseCommand

MY_ID = os.getenv('TELEGRAM_MY_ID')


class Command(BaseCommand):
    URL = 'https://api.telegram.org/'
    Token = os.getenv('TELEGRAM_TOKEN')

    def handle(self, *args, **options):

        requests.post(url=f'{self.URL}bot{self.Token}/sendMessage',
                      data={'chat_id': MY_ID,
                            'text': 'Вы подписались на курс!'
                            },)

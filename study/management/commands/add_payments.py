from django.core.management import BaseCommand
from users.models import Payment, User


class Command(BaseCommand):
    def handle(self, *args, **options):
        payment_list = [
            {'user': User.objects.get(email='admin')}
        ]

        for payment in payment_list:
            Payment.objects.create(**payment)

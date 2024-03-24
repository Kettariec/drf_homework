from celery import shared_task
from django.utils import timezone
from calendar import monthrange
from datetime import datetime, timedelta
from users.models import User


@shared_task
def check_user_activity():
    now = datetime.now(tz=timezone.utc)
    month = now.month
    year = now.year
    days_count = monthrange(year, month)
    expiration_date = now - timedelta(days=days_count[1])
    user_list = User.objects.filter(last_login__lte=expiration_date, is_active=True)
    user_list.update(is_active=False)

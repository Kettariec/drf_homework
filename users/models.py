from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='почта пользователя')
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    city = models.CharField(max_length=35, verbose_name='город', **NULLABLE)
    avatar = models.ImageField(upload_to='users/',
                               verbose_name='аватар', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Payment(models.Model):

    class PaymentType(models.TextChoices):
        CASH = "CASH", "Наличные"
        TRANSFER_TO_ACCOUNT = 'TRANSFER_TO_ACCOUNT', 'Перевод на счет'

    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name='пользователь', related_name='user')
    date = models.DateField(auto_now_add=True,
                            verbose_name='дата платежа')
    paid_course = models.ForeignKey('study.Course',
                                    on_delete=models.CASCADE, **NULLABLE,
                                    verbose_name='оплаченный курс',
                                    related_name='payment')
    paid_lesson = models.ForeignKey('study.Lesson',
                                    on_delete=models.CASCADE, **NULLABLE,
                                    verbose_name='оплаченный урок',
                                    related_name='payment')
    sum = models.DecimalField(max_digits=10, decimal_places=2,
                              verbose_name='Сумма оплаты', **NULLABLE)
    type = models.CharField(max_length=20, verbose_name='способ оплаты',
                            choices=PaymentType.choices,
                            default='TRANSFER_TO_ACCOUNT')

    def __str__(self):
        return f'{self.user} - {self.date}'

    class Meta:
        verbose_name = 'платёж'
        verbose_name_plural = 'платёжи'

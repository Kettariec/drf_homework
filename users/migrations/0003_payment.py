# Generated by Django 5.0.2 on 2024-02-24 19:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0002_alter_lesson_course'),
        ('users', '0002_remove_user_username_user_avatar_user_city_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, verbose_name='дата платежа')),
                ('sum', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Сумма оплаты')),
                ('type', models.CharField(choices=[('CASH', 'Наличные'), ('TRANSFER_TO_ACCOUNT', 'Перевод на счет')], default='TRANSFER_TO_ACCOUNT', max_length=20, verbose_name='способ оплаты')),
                ('paid_course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='study.course', verbose_name='оплаченный курс')),
                ('paid_lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='study.lesson', verbose_name='оплаченный урок')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'платёж',
                'verbose_name_plural': 'платёжи',
            },
        ),
    ]

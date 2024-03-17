from django.db import models
from django.conf import settings

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name='название курса')
    image = models.ImageField(upload_to='course/',
                              verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)

    owner = models.ForeignKey('users.User', on_delete=models.CASCADE,
                              verbose_name='Владелец', default=1)
    price = models.PositiveIntegerField(verbose_name='цена', default=0)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=50, verbose_name='название урока')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    image = models.ImageField(upload_to='course/',
                              verbose_name='превью', **NULLABLE)
    video = models.URLField(max_length=200,
                            verbose_name='ссылка на видео', **NULLABLE)

    course = models.ForeignKey('Course', on_delete=models.CASCADE,
                               verbose_name='курс', **NULLABLE,
                               related_name='lessons')

    owner = models.ForeignKey('users.User', on_delete=models.CASCADE,
                              verbose_name='Владелец', default=1)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Subscription(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE,
                               verbose_name='Курс', related_name='subscription')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             verbose_name='Пользователь', related_name='subscription')

    def __str__(self):
        return f'{self.user} - {self.course}'

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'

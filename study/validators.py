import re
from rest_framework.serializers import ValidationError


class UrlValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg = re.compile('^https://www.youtube.com/')
        field_value = dict(value).get(self.field)
        if not bool(reg.match(field_value)):
            raise ValidationError('Ссылки на уроки могут быть только с платформы youtube')

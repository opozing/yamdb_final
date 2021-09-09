from datetime import datetime

from django.core.exceptions import ValidationError


def year_validation(value):
    if value > datetime.now().year:
        raise ValidationError('Дата не может быть больше текущей даты')

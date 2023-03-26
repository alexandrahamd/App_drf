import datetime

from rest_framework import serializers
import request
from rest_framework.generics import get_object_or_404

from users.models import User


class BlogAgeValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        user = value.get('user')
        obj_user = get_object_or_404(User, email=user)
        date_now = datetime.datetime.now().date()
        age = date_now.year - obj_user.date_of_birth.year
        if age < 18:
            raise serializers.ValidationError('Вы еще слишком молоды')


class BlogWordsValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value,):
        bad_words = ['ерунда', 'глупость', 'чепуха']
        title = value.get('title').lower()
        split_title = title.split()
        print(split_title)

        for item in split_title:
            if item in bad_words:
                message = 'Вы использовали запрещенные слова'
                raise serializers.ValidationError(message)






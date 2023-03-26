from rest_framework import serializers


class EmailValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        email = value.get('email')
        if not email.endswith(('mail.ru', 'yandex.ru')):
            raise serializers.ValidationError('Можно использовать только: mail.ru, yandex.ru')


class PasswordValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        password = value.get('password')
        if len(password) < 8:
            raise serializers.ValidationError(f'Пароль должен быть от 8 знаков')
        if not any(x.isdigit() for x in password):
            raise serializers.ValidationError('Пароль должен включать цифры')
        return password

import datetime

from rest_framework import serializers
from rest_framework.serializers import raise_errors_on_nested_writes
from rest_framework.utils import model_meta

from users.models import User
from users.validators import EmailValidator, PasswordValidator


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'date_of_birth', 'password')
        validators = [EmailValidator(field='email'), PasswordValidator(field='password')]

    def create(self, validated_data):
        user = super().create(validated_data)
        user.date_of_change = datetime.datetime.now()
        user.set_password(validated_data['password'])

        user.is_active = True
        user.save()
        return user

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        # raise_errors_on_nested_writes('update', self, validated_data)
        # info = model_meta.get_field_info(instance)
        # m2m_fields = []
        # for attr, value in validated_data.items():
        #     if attr in info.relations and info.relations[attr].to_many:
        #         m2m_fields.append((attr, value))
        #     else:
        #         setattr(instance, attr, value)
        user.date_of_change = datetime.datetime.now()
        user.save()
        instance.save()


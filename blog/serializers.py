import datetime

from rest_framework import serializers
from blog.models import Blog
from blog.validators import BlogAgeValidator, BlogWordsValidator
from comments.serializers import CommentSerializer


class BlogSerializer(serializers.ModelSerializer):
    comments_all = CommentSerializer(required=False, many=True, source='comment_set')
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Blog
        fields = ('title', 'content', 'image', 'comments_all', 'user')
        validators = [BlogWordsValidator(field='title'), BlogAgeValidator(field="user")]

    def update(self, instance, validated_data):
        obj = super().update(instance, validated_data)
        obj.date_of_change = datetime.datetime.now()
        obj.save()
        instance.save()
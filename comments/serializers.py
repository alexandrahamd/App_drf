import datetime

from rest_framework import serializers
from comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('context', )

    def update(self, instance, validated_data):
        obj = super().update(instance, validated_data)
        obj.date_of_change = datetime.datetime.now()
        obj.save()
        instance.save()
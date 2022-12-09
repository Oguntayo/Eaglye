from rest_framework import serializers
from trends.models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('__all__')  # ['recipient', 'name', 'body']

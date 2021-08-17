from Users.serializers.UserSerializers import UserGetSerializer
from Messages.models import Message
from rest_framework import serializers


class MessageViewSerializer(serializers.ModelSerializer):
    sender = UserGetSerializer(many=False)
    receiver = UserGetSerializer(many=False)

    class Meta:
        model = Message
        fields = '__all__'


class MessageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

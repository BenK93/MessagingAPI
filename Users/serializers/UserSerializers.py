from rest_framework import serializers
from Users.models import CustomUser


class UserGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'username']


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']

    # def create(self, validated_data):
    #     user = CustomUser.objects.create(
    #         username=validated_data['username'], email=validated_data['email'])
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user

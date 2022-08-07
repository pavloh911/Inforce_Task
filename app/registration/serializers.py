from rest_framework import serializers
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class RegisterUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class RegisterRestaurantSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


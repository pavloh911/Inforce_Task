from rest_framework import serializers
from .models import Menu, Voting


class MenuCreateSerializer(serializers.ModelSerializer):
    restaurant = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Menu
        fields = ('restaurant', 'menu', 'data')


class MenuShowSerializer(serializers.ModelSerializer):
    restaurant = serializers.CharField(source='restaurant.username')

    class Meta:
        model = Menu
        fields = ('restaurant', 'menu', 'data')


class VotingChoiceSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Voting
        fields = ('restaurant', 'user')


class VotingAdminSerializer(serializers.ModelSerializer):
    restaurant = serializers.CharField(source='restaurant.username')
    user = serializers.CharField(source='user.username')

    class Meta:
        model = Voting
        fields = ('restaurant', 'user')


class VotingResultSerializer(serializers.Serializer):
    restaurant__username = serializers.CharField(max_length=200)
    total = serializers.IntegerField()



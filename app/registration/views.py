from django.contrib.auth.models import User, Group
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RegisterUserSerializer, RegisterRestaurantSerializer

from django.contrib.auth import get_user_model  # If used custom user model

UserModel = get_user_model()


class RegisterUserAPI(APIView):
    serializer_class = RegisterUserSerializer

    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        User.objects.create_user(username=request.data['username'], password=request.data['password'])
        try:
            user = User.objects.get(username=request.data['username'])
            user_group = Group.objects.get(name='user')
            user_group.user_set.add(user)
        except:
            pass
        return Response({'post': serializer.data})


class RegisterRestaurantAPI(APIView):
    serializer_class = RegisterRestaurantSerializer

    def post(self, request):
        serializer = RegisterRestaurantSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        User.objects.create_user(username=request.data['username'], password=request.data['password'])
        user = User.objects.get(username=request.data['username'])
        user_group = Group.objects.get(name='restaurant')
        user_group.user_set.add(user)
        return Response({'post': serializer.data})

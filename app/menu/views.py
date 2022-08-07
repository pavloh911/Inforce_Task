import datetime
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from django.db.models import Count

from .models import Menu, Voting
from .serializers import MenuCreateSerializer, MenuShowSerializer, VotingChoiceSerializer, VotingResultSerializer, \
    VotingAdminSerializer
from .permissions import AddMenuForRestaurant, ShowMenusForUsers, IfNotVoted, IsAdmin


class MenuAPICreate(generics.CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuCreateSerializer
    permission_classes = (AddMenuForRestaurant,)


class MenuAPIList(generics.ListAPIView):
    queryset = Menu.objects.filter(data=datetime.date.today())
    serializer_class = MenuShowSerializer
    permission_classes = (ShowMenusForUsers,)


class VotingAPI(mixins.CreateModelMixin,
                GenericViewSet):
    serializer_class = VotingChoiceSerializer
    permission_classes = (IfNotVoted,)


class VotingAdminAPI(generics.ListAPIView):
    queryset = Voting.objects.filter(data=datetime.date.today())
    serializer_class = VotingAdminSerializer
    permission_classes = (IsAdmin,)


class VotingResultAPI(APIView):
    permission_classes = (IsAdmin,)

    def get(self, request):
        today = Voting.objects.filter(data=datetime.date.today())
        res = today.values('restaurant__username').annotate(total=Count('restaurant')).order_by('total')
        return Response({'posts': VotingResultSerializer(res, many=True).data})

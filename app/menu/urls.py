from django.urls import path
from .views import MenuAPIList, MenuAPICreate, VotingAPI, VotingResultAPI, VotingAdminAPI

urlpatterns = [
    path('result/', VotingResultAPI.as_view()),
    path('voting/admin/', VotingAdminAPI.as_view()),
    path('voting/', VotingAPI.as_view({'post': 'create'})),
    path('list/', MenuAPIList.as_view()),
    path('create/', MenuAPICreate.as_view())
]

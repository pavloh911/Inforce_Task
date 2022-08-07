from django.urls import path
from .views import RegisterUserAPI, RegisterRestaurantAPI

urlpatterns = [
    path('user/', RegisterUserAPI.as_view()),
    path('restaurant/', RegisterRestaurantAPI.as_view()),
]

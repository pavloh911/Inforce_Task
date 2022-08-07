from django.contrib.auth.models import User
from django.db import models
import datetime


class Menu(models.Model):
    restaurant = models.ForeignKey(User, on_delete=models.CASCADE)
    menu = models.TextField()
    data = models.DateField(default=datetime.date.today())

    def __str__(self):
        return str(self.restaurant)


class Voting(models.Model):
    restaurant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='restaurant')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    data = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.restaurant)

import datetime
from rest_framework import permissions

from .models import Voting


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)


class AddMenuForRestaurant(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='restaurant').exists():
            return True
        return False


class ShowMenusForUsers(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='user').exists():
            return True
        return False


class IfNotVoted(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='user').exists():
            try:
                if request.user == Voting.objects.get(data=datetime.date.today()):
                    return False
            except:
                return True
        return False

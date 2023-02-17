from rest_framework import permissions
from rest_framework.views import Request, View
import ipdb

class IsSuperUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        if request.method == "GET":
            return True
        if request.user.is_authenticated and request.user.is_superuser:
            return True

class IsUserOnly(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj):
        if request.user.is_superuser:
            return True
        return request.user == obj
    
class IsNotSuperUser(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        if request.user.is_authenticated:
            return True
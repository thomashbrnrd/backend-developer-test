from rest_framework import permissions

from shopping.models import ShoppingList


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsShoppingListOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if "shopping_list" in request.data:
            shopping_list = ShoppingList.objects.get(id=request.data["shopping_list"])
            return shopping_list.user == request.user
        return True

    def has_object_permission(self, request, view, obj):
        return obj.shopping_list.user == request.user

from rest_framework import viewsets, mixins, permissions

from api.permissions import IsOwner, IsShoppingListOwner

from .models import ShoppingList, ShoppingListItem
from .serializers import ShoppingListSerializer, ShoppingListItemSerializer

class ShoppingListViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):

    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer
    permission_classes = [permissions.IsAuthenticated & IsOwner]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

class ShoppingListItemViewSet(mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        viewsets.GenericViewSet):

    queryset = ShoppingListItem.objects.all()
    serializer_class = ShoppingListItemSerializer
    permission_classes = [permissions.IsAuthenticated & IsShoppingListOwner]

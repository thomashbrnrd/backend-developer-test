from rest_framework import serializers

from .models import ShoppingList, ShoppingListItem

class ShoppingListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingListItem
        fields = "__all__"

class ShoppingListSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )
    items = ShoppingListItemSerializer(read_only=True, many=True)
    total_cost = serializers.DecimalField(read_only=True, max_digits=19, decimal_places=2)

    class Meta:
        model = ShoppingList
        fields = "__all__"

from rest_framework import serializers

from ingredient.serializers import IngredientSerializer

from .models import ShoppingList, ShoppingListItem

class ShoppingListItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShoppingListItem
        fields = "__all__"

class ShoppingListItemReadOnlySerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer(read_only=True)

    class Meta:
        model = ShoppingListItem
        fields = ("id", "ingredient", "quantity")

class ShoppingListSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )
    items = ShoppingListItemReadOnlySerializer(read_only=True, many=True)
    total_cost = serializers.DecimalField(read_only=True, max_digits=19, decimal_places=2)

    class Meta:
        model = ShoppingList
        fields = "__all__"

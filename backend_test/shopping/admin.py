from django.contrib import admin

from shopping.models import (
    ShoppingList,
    ShoppingListItem,
)


@admin.register(ShoppingListItem)
class ShoppingListItemAdmin(admin.ModelAdmin):
    pass


@admin.register(ShoppingList)
class ShoppingListAdmin(admin.ModelAdmin):
    pass

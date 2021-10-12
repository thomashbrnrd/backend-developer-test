import factory

from api.factories import UserFactory
from ingredient.factories import IngredientFactory


class ShoppingListFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "shopping.ShoppingList"
        django_get_or_create = ("title", "user")

    title = factory.Faker("word")
    user = factory.SubFactory(UserFactory)


class ShoppingListItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "shopping.ShoppingListItem"
        django_get_or_create = ("shopping_list", "ingredient", "quantity")

    shopping_list = factory.SubFactory(ShoppingListFactory)
    ingredient = factory.SubFactory(IngredientFactory)
    quantity = factory.Faker("pyint")

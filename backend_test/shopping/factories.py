import factory

from api.factories import UserFactory

class ShoppingListFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'shopping.ShoppingList'
        django_get_or_create = ('title', 'user')

    title = factory.Faker('word')
    user = factory.SubFactory(UserFactory)

import factory

class IngredientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'ingredient.Ingredient'  # Equivalent to ``model = myapp.models.User``
        django_get_or_create = ('name',)

    name = factory.Faker('word')

import json

from faker import Faker
fake = Faker()

from django.contrib.auth import get_user_model
from django.db import migrations

def get_models(apps):
    ShoppingListItem = apps.get_model("shopping", "ShoppingListItem")
    ShoppingList = apps.get_model("shopping", "ShoppingList")
    Ingredient = apps.get_model("ingredient", "Ingredient")
    User = get_user_model()
    return ShoppingListItem, ShoppingList, Ingredient, User

def load_shoppinglists_from_json(apps, schema_editor):
    with open("data/shopping_lists.json") as json_file:
        shoppinglist_items = json.load(json_file)
        ShoppingListItem, ShoppingList, Ingredient, User = get_models(apps)
        initial_items = []
        for item in shoppinglist_items:
            try:
                shopping_list = ShoppingList.objects.get(
                    title=item["Shopping List"]
                )
            except ShoppingList.DoesNotExist as e:
                fake_user = fake.simple_profile()
                while User.objects.filter(username=fake_user["username"]).exists():
                    fake_user = fake.simple_profile()
                shopping_list = ShoppingList.objects.create(
                    title=item["Shopping List"],
                    user_id=User.objects.create_user(
                        username=fake_user["username"],
                        email=fake_user["username"] + "@fake.com",
                        first_name=fake_user["name"].split()[0],
                        last_name=fake_user["name"].split()[1]
                    ).id
                )
            ingredient = Ingredient.objects.get(name=item["Ingredient"])
            initial_items.append(
                ShoppingListItem(
                    quantity=item["Amount"],
                    ingredient=ingredient,
                    shopping_list=shopping_list,
                )
            )

        ShoppingListItem.objects.bulk_create(initial_items)


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("shopping", "0001_initial"),
        ("ingredient", "0002_seed"),
    ]

    operations = [
        migrations.RunPython(load_shoppinglists_from_json),
    ]

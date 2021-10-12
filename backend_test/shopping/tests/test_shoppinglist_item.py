import pytest

from django.urls import reverse

from rest_framework.test import APIClient

from api.factories import UserFactory
from ingredient.factories import IngredientFactory
from shopping.models import ShoppingList
from shopping.factories import ShoppingListFactory, ShoppingListItemFactory

@pytest.fixture
def client():
    return APIClient()

class TestShoppingListItem:

    def url(self, pk = None):
        if pk:
            return reverse('shoppinglistitem-detail', args=[pk])
        else:
            return reverse('shoppinglistitem-list')

    # SUCCESS
    @pytest.mark.django_db
    def test_create(self, client, faker):
        ingredient = IngredientFactory()
        shopping_list = ShoppingListFactory()
        client.force_authenticate(user=shopping_list.user)
        data = {
            "ingredient": ingredient.id,
            "shopping_list": shopping_list.id,
            "quantity": 12
        }
        response = client.post(self.url(), data, format='json')
        print(response.json())
        assert response.status_code == 201
        assert "ingredient" in response.json()
        assert "shopping_list" in response.json()
        assert "quantity" in response.json()

    @pytest.mark.django_db
    def test_update(self, client, faker):
        shopping_list_item = ShoppingListItemFactory(quantity=faker.pyint())
        client.force_authenticate(user=shopping_list_item.shopping_list.user)
        data = {
            "quantity": faker.pyint(),
        }
        response = client.patch(self.url(shopping_list_item.id), data, format='json')

        assert response.status_code == 200
        assert "ingredient" in response.json()
        assert "shopping_list" in response.json()
        assert "quantity" in response.json()
        assert response.json()["quantity"] == data["quantity"]


    # ERRORS
    @pytest.mark.django_db
    def test_create_no_auth(self, client, faker):
        response = client.post(self.url(), {}, format='json')
        assert response.status_code == 401

    @pytest.mark.django_db
    def test_create_missing_field(self, client):
        user = UserFactory()
        client.force_authenticate(user=user)
        response = client.post(self.url(), {}, format='json')
        assert response.status_code == 400
        assert "ingredient" in response.json()
        assert "shopping_list" in response.json()
        assert "quantity" in response.json()

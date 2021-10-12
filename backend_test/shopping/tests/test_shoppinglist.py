import pytest

from django.urls import reverse

from rest_framework.test import APIClient

from api.factories import UserFactory

from shopping.factories import ShoppingListFactory

@pytest.fixture
def client():
    return APIClient()

class TestShoppingList:

    def url(self, pk = None):
        if pk:
            return reverse('ShoppingList-detail', args=[pk])
        else:
            return reverse('ShoppingList-list')

    # SUCCESS
    @pytest.mark.django_db
    def test_create(self, client, faker):
        user = UserFactory()
        client.force_authenticate(user=user)
        data = {
            "title": faker.word()
        }
        response = client.post(self.url(), data, format='json')

        assert response.status_code == 201

    @pytest.mark.django_db
    def test_retrieve(self, client, faker):
        shoppinglist = ShoppingListFactory()
        client.force_authenticate(user=shoppinglist.user)
        response = client.get(self.url(shoppinglist.id), format='json')

        assert response.status_code == 200
        assert "items" in response.json()
        assert "total_cost" in response.json()

    @pytest.mark.django_db
    def test_update(self, client, faker):
        shoppinglist = ShoppingListFactory()
        client.force_authenticate(user=shoppinglist.user)
        data = {
            "title": faker.word()
        }
        response = client.patch(self.url(shoppinglist.id), data, format='json')
        assert response.status_code == 200
        assert response.json()["title"] == data["title"]


    # ERRORS
    @pytest.mark.django_db
    def test_create_no_auth(self, client):
        data = {}
        response = client.post(self.url(), data, format='json')

        assert response.status_code == 401

    @pytest.mark.django_db
    def test_create_missing_field(self, client):
        user = UserFactory()
        client.force_authenticate(user=user)
        response = client.post(self.url(), {}, format='json')
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_retrieve_wrong_user(self, client, faker):
        shoppinglist = ShoppingListFactory()
        wrong_user = UserFactory()
        client.force_authenticate(user=wrong_user)
        response = client.get(self.url(shoppinglist.id), format='json')

        assert response.status_code == 404

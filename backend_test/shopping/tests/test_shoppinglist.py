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
            return reverse('shoppinglists-detail', args=[pk])
        else:
            return reverse('shoppinglists-list')

    # SUCCESS
    @pytest.mark.django_db
    def test_create(self, client, faker):
        user = UserFactory()
        data = {
            "title": faker.word()
        }
        response = client.post(self.url(), data, format='json')
        print(response.json())
        assert response.status_code == 201
        assert "name" in response.json()
        assert "category" in response.json()
        assert "unit" in response.json()

    @pytest.mark.django_db
    def test_update(self, client, faker):
        shoppinglist = ShoppingListFactory()
        data = {
            "title": faker.word()
        }
        response = client.patch(self.url(), data, format='json')
        assert response.status_code == 201
        assert response.json()["unit"] == data["unit"]
        assert response.json()["is_available"] == data["is_available"]
        assert response.json()["category"] == data["category"]


    # ERRORS
    @pytest.mark.django_db
    def test_create_no_auth(self, client):
        data = {}
        response = client.post(self.url(), data, format='json')

        assert response.status_code == 401
        assert "name" in response.json()
        assert "category" in response.json()
        assert "unit" in response.json()

    @pytest.mark.django_db
    def test_create_missing_field(self, client):
        data = {}
        response = client.post(self.url(), data, format='json')

        assert response.status_code == 401

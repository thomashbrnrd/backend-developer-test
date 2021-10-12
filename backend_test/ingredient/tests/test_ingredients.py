import pytest

from django.urls import reverse

from rest_framework.test import APIClient

from ingredient import choices
from ingredient.models import Ingredient
from ingredient.factories import IngredientFactory

@pytest.fixture
def client():
    return APIClient()

class TestIngredients:

    def url(self, pk = None):
        if pk:
            return reverse('Ingredient-detail', args=[pk])
        else:
            return reverse('Ingredient-list')

    # SUCCESS
    @pytest.mark.django_db
    def test_create(self, client, faker):
        data = {
            "name": faker.word(),
            "category": faker.word(ext_word_list=list(zip(*choices.CATEGORIES))[0]),
            "unit": faker.word(ext_word_list=list(zip(*choices.UNITS))[0]),
        }
        response = client.post(self.url(), data, format='json')
        print(response.json())
        assert response.status_code == 201
        assert "name" in response.json()
        assert "category" in response.json()
        assert "unit" in response.json()

    @pytest.mark.django_db
    def test_update(self, client, faker):
        ingredient = IngredientFactory(is_available=True)
        data = {
            "name": faker.word(),
            "category": faker.word(ext_word_list=list(zip(*choices.CATEGORIES))[0]),
            "unit": faker.word(ext_word_list=list(zip(*choices.UNITS))[0]),
            "is_available": False,
        }
        response = client.patch(self.url(ingredient.id), data, format='json')

        assert response.status_code == 200
        assert response.json()["unit"] == data["unit"]
        assert response.json()["is_available"] == data["is_available"]
        assert response.json()["category"] == data["category"]


    # ERRORS
    @pytest.mark.django_db
    def test_create_missing_field(self, client):
        response = client.post(self.url(), {}, format='json')

        assert response.status_code == 400
        assert "name" in response.json()
        assert "category" in response.json()
        assert "unit" in response.json()

    @pytest.mark.django_db
    def test_delete_not_allowed(self, client):
        ingredient = IngredientFactory(is_available=True)
        response = client.delete(self.url(ingredient.id), format='json')

        assert response.status_code == 405

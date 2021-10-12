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

    # SUCCESS
    @pytest.mark.django_db
    def test_create(self, client, faker):
        url = reverse('ingredient-list')
        data = {
            "name": faker.word(),
            "category": faker.word(ext_word_list=list(zip(*choices.CATEGORIES))[0]),
            "unit": faker.word(ext_word_list=list(zip(*choices.UNITS))[0]),
        }
        response = client.post(url, data, format='json')
        print(response.json())
        assert response.status_code == 201
        assert "name" in response.json()
        assert "category" in response.json()
        assert "unit" in response.json()

    @pytest.mark.django_db
    def test_update(self, client, faker):
        ingredient = IngredientFactory(is_available=True)
        url = reverse('ingredient-detail', args=[
            ingredient.id
        ])
        data = {
            "name": faker.word(),
            "category": faker.word(ext_word_list=list(zip(*choices.CATEGORIES))[0]),
            "unit": faker.word(ext_word_list=list(zip(*choices.UNITS))[0]),
        }
        response = client.patch(url, data, format='json')
        print(response.json())
        assert response.status_code == 200
        assert "name" in response.json()
        assert "category" in response.json()
        assert "unit" in response.json()


    # ERRORS
    @pytest.mark.django_db
    def test_create_missing_field(self, client):
        url = reverse('ingredient-list')
        data = {}
        response = client.post(url, data, format='json')

        assert response.status_code == 400
        assert "name" in response.json()
        assert "category" in response.json()
        assert "unit" in response.json()

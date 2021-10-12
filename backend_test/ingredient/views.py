from rest_framework import viewsets
from rest_framework import mixins

from .models import Ingredient
from .serializers import IngredientSerializer

class IngredientViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

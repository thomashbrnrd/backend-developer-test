from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from rest_framework import routers, permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from ingredient.views import IngredientViewSet
from shopping.views import ShoppingListViewSet, ShoppingListItemViewSet

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = routers.SimpleRouter()
router.register(r'ingredients', IngredientViewSet, basename='Ingredient')
router.register(r'shoppinglists', ShoppingListViewSet, basename='ShoppingList')
router.register(r'shoppinglistitems', ShoppingListItemViewSet, basename='ShoppingListItem')

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]

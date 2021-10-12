from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from rest_framework import routers

from ingredient.views import IngredientViewSet

router = routers.SimpleRouter()
router.register(r'ingredients', IngredientViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]

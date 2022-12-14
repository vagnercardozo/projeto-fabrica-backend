from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjetoViewSet
router = DefaultRouter()
router.register('projetos', ProjetoViewSet)

urlpatterns = [
    path("", include(router.urls))
]
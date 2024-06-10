
from django.urls import path, include
from .views import CardViewSet, ServiceViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('card', CardViewSet, basename='card')
router.register('Service', ServiceViewSet, basename='card')

urlpatterns = [
    path('', include(router.urls)),
]
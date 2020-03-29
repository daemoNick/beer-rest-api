from django.urls import path, include
from rest_framework.routers import DefaultRouter

from beer_api import views

router = DefaultRouter()
router.register('beer', views.BeerView)

urlpatterns = [
    path('', include(router.urls))
]
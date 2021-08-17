
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from .views import MessageViewSet

router = routers.DefaultRouter()

router.register('', MessageViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

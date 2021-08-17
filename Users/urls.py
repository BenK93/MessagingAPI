
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet

router = routers.DefaultRouter()

router.register('', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    # path('<pk>/', UserViewSet.as_view()),
]

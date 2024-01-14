# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerQueryViewSet

router = DefaultRouter()
router.register(r'query', CustomerQueryViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tour_api import views


router = DefaultRouter()
router.register(r'tours', views.PackageViewSet)

urlpatterns = [
    path('', include(router.urls))
]

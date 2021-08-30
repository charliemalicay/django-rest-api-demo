from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tour_api import views


router = DefaultRouter()
router.register(r'packages', views.PackageViewSet)
router.register(r'bookings', views.BookingViewSet)

urlpatterns = [
    path('', include(router.urls))
]

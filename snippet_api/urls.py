from django.urls import path, include
from rest_framework.routers import DefaultRouter

from snippet_api import views


router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)

urlpatterns = [
    path('', include(router.urls))
]

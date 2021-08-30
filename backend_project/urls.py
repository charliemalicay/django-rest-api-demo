from django.urls import path, include


urlpatterns = [
    path('api/v1/', include('user_api.urls')),
    path('api/v1/', include('snippet_api.urls')),
    path('api/v1/', include('tour_api.urls')),
    path('api-auth/', include('rest_framework.urls'))
]

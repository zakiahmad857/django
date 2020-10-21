from django.urls import include, path
from rest_framework import routers
from . import views

import user.api_views

router = routers.DefaultRouter()
router.register(r'juduls', views.JudulViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/juduls/', user.api_views.JudulList.as_view())
]

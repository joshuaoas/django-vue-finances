from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import SaveViewSet

router = DefaultRouter()

router.register('save', SaveViewSet, basename='save')

urlpatterns = [
    path('', include(router.urls)),
]

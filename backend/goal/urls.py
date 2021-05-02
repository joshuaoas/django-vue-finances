from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import GoalViewSet

router = DefaultRouter()

router.register('goal', GoalViewSet, basename='goal')

urlpatterns = [
    path('', include(router.urls)),
]

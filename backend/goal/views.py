from django.shortcuts import render

from rest_framework import viewsets

from .models import Goal

from .serializers import GoalSerializer


class GoalViewSet(viewsets.ModelViewSet):
    serializer_class = GoalSerializer
    queryset = Goal.objects.all()

    # only get Goals you created
    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)

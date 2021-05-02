from django.shortcuts import render

from rest_framework import viewsets

from .models import Income

from .serializers import IncomeSerializer


class IncomeViewSet(viewsets.ModelViewSet):
    serializer_class = IncomeSerializer
    queryset = Income.objects.all()

    # only get leads you created
    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)

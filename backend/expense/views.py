from django.shortcuts import render

from rest_framework import viewsets

from .models import Expense
from .models import Category

from .serializers import ExpenseSerializer
from .serializers import CategorySerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()

    # only get Expenses you created
    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    # only get categories you created
    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)

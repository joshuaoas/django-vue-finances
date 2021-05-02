from rest_framework import serializers


from .models import Expense
from .models import Category


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        read_only_fields = (
            'created_by',
            'created_at',
            'modified_at',
        ),
        fields = (
            'id',
            'title',
            'cost',
            'description',
            'date',
            'timestamp',
            'category',
            'user',
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        read_only_fields = (
            'created_by',
            'created_at',
            'modified_at',
        ),
        fields = (
            'id',
            'title',
            'user',
        )

from rest_framework import serializers


from .models import Income


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        read_only_fields = (
            'created_by',
            'created_at',
            'modified_at',
        ),
        fields = (
            'id',
            'title',
            'income',
            'date',
            'timestamp',
            'user',
        )

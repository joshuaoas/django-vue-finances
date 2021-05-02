from rest_framework import serializers


from .models import Goal


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        read_only_fields = (
            'created_by',
            'created_at',
            'modified_at',
        ),
        fields = (
            'id',
            'title',
            'description',
            'savings_needed',
            'date',
            'timestamp',
            'user',
        )

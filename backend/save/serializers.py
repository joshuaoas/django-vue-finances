from rest_framework import serializers


from .models import Save


class SaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Save
        read_only_fields = (
            'created_by',
            'created_at',
            'modified_at',
        ),
        fields = (
            'id',
            'title',
            'savings',
            'date',
            'timestamp',
            'user',
        )

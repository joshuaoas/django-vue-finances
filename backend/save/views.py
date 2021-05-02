from django.shortcuts import render

from rest_framework import viewsets

from .models import Save

from .serializers import SaveSerializer


class SaveViewSet(viewsets.ModelViewSet):
    serializer_class = SaveSerializer
    queryset = Save.objects.all()

    # only get Save you created
    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)

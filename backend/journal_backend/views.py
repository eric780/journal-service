from django.shortcuts import render
from rest_framework import viewsets
from .serializers import JournalEntryModelSerializer
from .models import JournalEntryModel

class JournalServiceView(viewsets.ModelViewSet):
    serializer_class = JournalEntryModelSerializer
    queryset = JournalEntryModel.objects.all()
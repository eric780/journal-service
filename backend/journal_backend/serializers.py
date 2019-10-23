from rest_framework import serializers
from .models import JournalEntryModel

class JournalEntryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalEntryModel
        fields = ('date', 'content')
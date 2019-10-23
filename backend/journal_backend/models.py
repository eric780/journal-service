from datetime import date
from django.db import models

# Create your models here.

class JournalEntryModel(models.Model):
    date = models.CharField(max_length=10)
    content = models.TextField()

    def __str__(self):
        return self._to_string()

    def _to_string(self) -> str:
        return self.date + " " + self.content

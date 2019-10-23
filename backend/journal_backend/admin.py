from django.contrib import admin
from .models import JournalEntryModel

# Register your models here.

class JournalEntryAdmin(admin.ModelAdmin):
    list_display = ('date', 'content')

admin.site.register(JournalEntryModel, JournalEntryAdmin)
# myapp/admin.py
from django.contrib import admin
from .models import ClothingSearch

@admin.register(ClothingSearch)
class ClothingSearchAdmin(admin.ModelAdmin):
    list_display = ('country', 'gender', 'age', 'search_term', 'main_word', 'color', 'height', 'weight', 'waist', 'chest', 'hip')
    search_fields = ('country', 'gender', 'search_term', 'main_word', 'color')
    list_filter = ('country', 'gender', 'age')

from django.contrib import admin
from .models import Category, Event

@admin.register(Category)
class Category(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Event)
class Event(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
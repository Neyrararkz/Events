from django.forms import ModelForm, TextInput, DateTimeInput, DecimalField, Select
from .models import Event

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'category', 'description', 'place', 'date_time', 'price']

        widgets = {
            "name": TextInput(attrs={
                "placeholder": "Название"
            }),            
            "description": TextInput(attrs={
                "placeholder": "Описание"
            }),            
            "place": TextInput(attrs={
                "placeholder": "Место"
            }),            
            "date_time": DateTimeInput(attrs={
                "placeholder": "Дата и время"
            })
        }
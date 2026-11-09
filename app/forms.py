from django.forms import ModelForm, TextInput, DateTimeInput, NumberInput, Select
from .models import Event

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['category', 'name', 'description', 'place', 'date_time', 'price']

        widgets = {   
            "category": Select(),   
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
                "type": "datetime-local"
            }),            
            "price": NumberInput(attrs={
                "placeholder": "Стоимость"
            })
        }
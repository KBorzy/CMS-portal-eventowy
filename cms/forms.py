from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'content', 'data_wydarzenia','ticket_quantity', 'ticket_price']
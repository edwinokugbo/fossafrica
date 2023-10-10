from dataclasses import field
from django import forms
from .models import Event, Participant


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'start_date', 'end_date', 'privacy', 'speakers',
                  'participants', 'anchor', 'location', 'location_name', 'event_status']
        widgets = {
            'start_date': forms.SelectDateWidget(),
            'end_date': forms.SelectDateWidget()
        }


class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'email']

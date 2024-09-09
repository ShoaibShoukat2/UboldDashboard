from django import forms
from django.core.exceptions import ValidationError

from ubold.apps.constants import CATEGORY_CHOICES


class EventForm(forms.Form):
    title = forms.CharField(max_length=255, required=True)
    className = forms.ChoiceField(choices=CATEGORY_CHOICES)
    start = forms.DateTimeField(required=True)
    allDay = forms.BooleanField(required=False)
    end = forms.DateTimeField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get("start")
        end = cleaned_data.get("end")
        if end and end < start:
            raise ValidationError("End date should be lessthen start date.")

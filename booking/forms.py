from django import forms
from .models import booking_device

class BookForm(forms.ModelForm):
    class Meta:
        model = booking_device
        fields = [
            "starting_point",
            "arrival_point",
        ]
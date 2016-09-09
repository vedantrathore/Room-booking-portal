from bootstrap3_datetime.widgets import DateTimePicker
from django import forms
from .models import *


class BookForm(forms.ModelForm):
    class Meta:
        model = Room_Booking
        fields = ['room_name','date', 'in_time', 'out_time']
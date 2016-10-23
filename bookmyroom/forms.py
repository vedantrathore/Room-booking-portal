from bootstrap3_datetime.widgets import DateTimePicker
from django import forms
from .models import *


class BookForm(forms.ModelForm):
    class Meta:
        model = Room_Booking
        fields = ['room_name','date', 'in_time', 'out_time']

        date= forms.DateInput(attrs={'id':'datepicker'}),
        in_time= forms.TimeInput(attrs={'id': 'timepicker'}),
        out_time= forms.TimeInput(attrs={'id': 'timepicker'}),


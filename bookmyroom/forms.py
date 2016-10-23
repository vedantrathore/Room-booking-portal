from bootstrap3_datetime.widgets import DateTimePicker
from django import forms
from .models import *


class BookForm(forms.ModelForm):
    class Meta:
        model = Room_Booking
        fields = ['room_name','date', 'in_time', 'out_time']

        date = forms.DateInput(attrs={'id':'datepicker'}),
        in_time = forms.TimeInput(attrs={'id': 'timepicker'}),
        out_time = forms.TimeInput(attrs={'id': 'timepicker'}),


    @property
    def validate_form(self):
            try:
                Room_Booking.objects.get(
                    room_name=self.cleaned_data['room_name'],
                    date=self.cleaned_data['date'],
                    in_time__lt= self.cleaned_data['in_time'],
                    out_time__gt= self.cleaned_data['out_time'])
                # if we get this far, we have an exact match for this form's data
                raise forms.ValidationError("Exists already!")
            except Room_Booking.DoesNotExist:
                # because we didn't get a match
                pass

            return self.cleaned_data

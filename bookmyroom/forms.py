from django import forms
from datetime import datetime
from .models import *


class BookForm(forms.ModelForm):
    class Meta:
        model = Room_Booking
        fields = ['room_name','date', 'in_time', 'out_time']
        widgets = {
            'date': forms.DateInput(attrs={'id':'datepicker'}),
        }

    def validate_form(self):
        name = self.cleaned_data.get('room_name')
        date = self.cleaned_data.get('date')
        in_time= self.cleaned_data.get('in_time')
        out_time= self.cleaned_data.get('out_time')
        room = Room_Booking.objects.filter(date=date).filter(room_name=name).order_by('in_time').filter(in_time__lte=out_time,out_time__gte=in_time).exists()
        if room:
            raise forms.ValidationError("Room not Available in this time period. Please check your dashboard")
        else:
            pass







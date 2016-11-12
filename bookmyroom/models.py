from django.db import models
from django.utils import timezone
from datetime import *


SERVER_CHOICES = (
    ('202.141.80.12', 'Teesta'),
    ('202.141.80.9', 'Naambor'),
    ('202.141.80.10', 'Disang'),
    ('202.141.80.11', 'Tamdil'),
    ('202.141.80.13', 'Dikrong')
)
class User(models.Model):
    username = models.CharField(max_length=35)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    server = models.CharField(max_length=10,choices=SERVER_CHOICES,default='Teesta')

    def __unicode__(self):
        return self.username


class Room(models.Model):
    ROOM_CHOICES = (
        ('Conference_Hall', 'Conference Hall'),
        ('Sports_Office', 'Sports Office'),
        ('room3', 'room3'),
        # add room here
    )
    # room_image = models.ImageField(null=True)
    room_name = models.TextField(choices=ROOM_CHOICES, default='Conference_Hall')
    room_occupancy = models.IntegerField(null=True)

    def __unicode__(self):
        return self.room_name


class Room_Booking(models.Model):
    TimeChoices = [
        (time(0,00), u'12:00 am'),
        (time(0,30), u'12:30 am'),
        (time(1,00), u'1:00 am'),
        (time(1,30), u'1:30 am'),
        (time(2,00), u'2:00 am'),
        (time(2,30), u'2:30 am'),
        (time(3,00), u'3:00 am'),
        (time(3,30), u'3:30 am'),
        (time(4,00), u'4:00 am'),
        (time(4,30), u'4:30 am'),
        (time(5,00), u'5:00 am'),
        (time(5,30), u'5:30 am'),
        (time(6,00), u'6:00 am'),
        (time(6,30), u'6:30 am'),
        (time(7,00), u'7:00 am'),
        (time(7,30), u'7:30 am'),
        (time(8,00), u'8:00 am'),
        (time(8,30), u'8:30 am'),
        (time(9,00), u'9:00 am'),
        (time(9,30), u'9:30 am'),
        (time(10,00), u'10:00 am'),
        (time(10,30), u'10:30 am'),
        (time(11,00), u'11:00 am'),
        (time(11,30), u'11:30 am'),
        (time(12,00), u'12:00 pm'),
        (time(12,30), u'12:30 pm'),
        (time(13,00), u'1:00 pm'),
        (time(13,30), u'1:30 pm'),
        (time(14,00), u'2:00 pm'),
        (time(14,30), u'2:30 pm'),
        (time(15,00), u'3:00 pm'),
        (time(15,30), u'3:30 pm'),
        (time(16,00), u'4:00 pm'),
        (time(16,30), u'4:30 pm'),
        (time(17,00), u'5:00 pm'),
        (time(17,30) ,u'5:30 pm'),
        (time(18,00), u'6:00 pm'),
        (time(18,30), u'6:30 pm'),
        (time(19,00), u'7:00 pm'),
        (time(19,30), u'7:30 pm'),
        (time(20,00), u'8:00 pm'),
        (time(20,30), u'8:30 pm'),
        (time(21,00), u'9:00 pm'),
        (time(21,30), u'9:30 pm'),
        (time(22,00), u'10:00 pm'),
        (time(22,30), u'10:30 pm'),
        (time(23,00), u'11:00 pm'),
        (time(23,30), u'11:30 pm'),

    ]
    room_name = models.ForeignKey(Room)
    room_status = models.BooleanField(default=False)
    date = models.DateField(blank=True, null=True)
    in_time = models.TimeField(blank=True, choices=TimeChoices, default='17:30')
    out_time = models.TimeField(blank=True, choices=TimeChoices, default='17:30')
    book_time = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.room_name.room_name

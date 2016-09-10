from django.db import models
from django.utils import timezone
from datetime import datetime

class User(models.Model):
    name = models.CharField(max_length=35)
    password = models.CharField(max_length=20)
    #rooms = models.ManyToManyField(Room)
    email = models.CharField(max_length=200)

    # rooms=models.ForeignKey(Room_Booking)

    def __unicode__(self):
        return self.name

class Room(models.Model):
    ROOM_CHOICES = (
        ('Conference_Hall', 'Conference Hall'),
        ('Sports_Office', 'Sports Office'),
        ('room3', 'room3'),
        #add room here
    )
    room_name = models.TextField(choices=ROOM_CHOICES,default='Conference_Hall')
    room_occupancy = models.IntegerField(null=True)

    def __unicode__(self):
        return self.room_name
    

class Room_Booking(models.Model):
    room_name = models.ForeignKey(Room)
    room_status = models.BooleanField(default=False)
    date = models.DateField(blank=True, null=True)
    in_time = models.TimeField(blank=True, null=True)
    out_time = models.TimeField(blank=True, null=True)
    book_time = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.room_name.room_name

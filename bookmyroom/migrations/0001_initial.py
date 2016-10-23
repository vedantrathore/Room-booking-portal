# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 10:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.TextField(choices=[(b'Conference_Hall', b'Conference Hall'), (b'Sports_Office', b'Sports Office'), (b'room3', b'room3')], default=b'Conference_Hall')),
                ('room_occupancy', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room_Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_status', models.BooleanField(default=False)),
                ('date', models.DateField(blank=True, null=True)),
                ('in_time', models.TimeField(blank=True, null=True)),
                ('out_time', models.TimeField(blank=True, null=True)),
                ('book_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('room_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmyroom.Room')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('password', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='room_booking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmyroom.User'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 10:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmyroom', '0004_auto_20161027_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room_booking',
            name='in_time',
            field=models.TimeField(blank=True, choices=[(b'00:00', b'12:00 am'), (b'00:30', b'12:30 am'), (b'01:00', b'1:00 am'), (b'01:30', b'1:30 am'), (b'02:00', b'2:00 am'), (b'02:30', b'2:30 am'), (b'03:00', b'3:00 am'), (b'03:30', b'3:30 am'), (b'04:00', b'4:00 am'), (b'04:30', b'4:30 am'), (b'05:00', b'5:00 am'), (b'05:30', b'5:30 am'), (b'06:00', b'6:00 am'), (b'06:30', b'6:30 am'), (b'07:00', b'7:00 am'), (b'07:30', b'7:30 am'), (b'08:00', b'8:00 am'), (b'08:30', b'8:30 am'), (b'09:00', b'9:00 am'), (b'09:30', b'9:30 am'), (b'10:00', b'10:00 am'), (b'10:30', b'10:30 am'), (b'11:00', b'11:00 am'), (b'11:30', b'11:30 am'), (b'12:00', b'12:00 pm'), (b'12:30', b'12:30 pm'), (b'13:00', b'1:00 pm'), (b'13:30', b'1:30 pm'), (b'14:00', b'2:00 pm'), (b'14:30', b'2:30 pm'), (b'15:00', b'3:00 pm'), (b'15:30', b'3:30 pm'), (b'16:00', b'4:00 pm'), (b'16:30', b'4:30 pm'), (b'17:00', b'5:00 pm'), (b'17:30', b'5:30 pm'), (b'18:00', b'6:00 pm'), (b'18:30', b'6:30 pm'), (b'19:00', b'7:00 pm'), (b'19:30', b'7:30 pm'), (b'20:00', b'8:00 pm'), (b'20:30', b'8:30 pm'), (b'21:00', b'9:00 pm'), (b'21:30', b'9:30 pm'), (b'22:00', b'10:00 pm'), (b'22:30', b'10:30 pm'), (b'23:00', b'11:00 pm'), (b'23:30', b'11:30 pm')], default=b'17:30'),
        ),
        migrations.AlterField(
            model_name='room_booking',
            name='out_time',
            field=models.TimeField(blank=True, choices=[(b'00:00', b'12:00 am'), (b'00:30', b'12:30 am'), (b'01:00', b'1:00 am'), (b'01:30', b'1:30 am'), (b'02:00', b'2:00 am'), (b'02:30', b'2:30 am'), (b'03:00', b'3:00 am'), (b'03:30', b'3:30 am'), (b'04:00', b'4:00 am'), (b'04:30', b'4:30 am'), (b'05:00', b'5:00 am'), (b'05:30', b'5:30 am'), (b'06:00', b'6:00 am'), (b'06:30', b'6:30 am'), (b'07:00', b'7:00 am'), (b'07:30', b'7:30 am'), (b'08:00', b'8:00 am'), (b'08:30', b'8:30 am'), (b'09:00', b'9:00 am'), (b'09:30', b'9:30 am'), (b'10:00', b'10:00 am'), (b'10:30', b'10:30 am'), (b'11:00', b'11:00 am'), (b'11:30', b'11:30 am'), (b'12:00', b'12:00 pm'), (b'12:30', b'12:30 pm'), (b'13:00', b'1:00 pm'), (b'13:30', b'1:30 pm'), (b'14:00', b'2:00 pm'), (b'14:30', b'2:30 pm'), (b'15:00', b'3:00 pm'), (b'15:30', b'3:30 pm'), (b'16:00', b'4:00 pm'), (b'16:30', b'4:30 pm'), (b'17:00', b'5:00 pm'), (b'17:30', b'5:30 pm'), (b'18:00', b'6:00 pm'), (b'18:30', b'6:30 pm'), (b'19:00', b'7:00 pm'), (b'19:30', b'7:30 pm'), (b'20:00', b'8:00 pm'), (b'20:30', b'8:30 pm'), (b'21:00', b'9:00 pm'), (b'21:30', b'9:30 pm'), (b'22:00', b'10:00 pm'), (b'22:30', b'10:30 pm'), (b'23:00', b'11:00 pm'), (b'23:30', b'11:30 pm')], default=b'17:30'),
        ),
    ]

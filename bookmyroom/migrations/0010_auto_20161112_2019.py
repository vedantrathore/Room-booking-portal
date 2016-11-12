# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmyroom', '0009_auto_20161112_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='server',
            field=models.TextField(default=b'Teesta', choices=[(b'202.141.80.12', b'Teesta'), (b'202.141.80.9', b'Naambor'), (b'202.141.80.10', b'Disang'), (b'202.141.80.11', b'Tamdil'), (b'202.141.80.13', b'Dikrong')]),
        ),
    ]

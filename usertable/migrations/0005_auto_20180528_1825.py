# Generated by Django 2.0.3 on 2018-05-28 18:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usertable', '0004_auto_20180528_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='when_registered',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 1, 0, 0)),
        ),
    ]

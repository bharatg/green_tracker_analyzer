# Generated by Django 2.0.3 on 2018-05-28 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usertable', '0003_auto_20180528_1821'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='uid',
            new_name='usr_id',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='usr_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='when_registered',
        ),
    ]

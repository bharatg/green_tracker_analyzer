from django.db import models

import datetime
import random

from django.utils.timezone import now

class User(models.Model):
    uid   = models.IntegerField(default=0, primary_key=True)
    name = models.CharField(max_length=200, default='')
    when_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'user: ' + str(self.name) + ', id: ' + str(self.uid) + ', registered: ' + str(self.when_registered)

    def query_all(self):
        return User.objects.all()

class Habit(models.Model):
    CHOICES = (
        ('B', 'bici'),
        ('P', 'piedi'),
        ('M', 'macchina'),
	('L', 'mezzi pubblici'),
	('X', 'macchina e mezzi pubblici')
    )

    usr_id = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
	default=0
    )
    time   = models.DateTimeField(auto_now_add=True)
    choice = models.CharField(max_length=200, choices=CHOICES, default='L')

    def __str__(self):
        return 'habit: ' + str(self.choice) + ', user: ' + str(self.usr_id) + ', time: ' + str(self.time)

    def query_all(self):
        return Habit.objects.all()

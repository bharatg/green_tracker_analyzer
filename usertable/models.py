from django.db import models

import random

class User(models.Model):
    usr_id   = models.IntegerField(default=0)
    usr_name = models.CharField(max_length=200)

    def __str__(self):
        return 'user: ' + str(self.usr_name) + ', id: ' + str(self.usr_id)

    def query_all(self):
        return User.objects.all()

class Habit(models.Model):
    hab_id     = models.IntegerField(default=0)
    hab_time   = models.DateTimeField('date published')
    hab_choice = models.CharField(max_length=200)

    def __str__(self):
        return 'habit: ' + str(self.hab_choice) + ', id: ' + str(self.hab_id) + ', time: ' + str(self.hab_time)

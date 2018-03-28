from django.db import models

class Users(models.Model):
    usr_id   = models.IntegerField(default=0)
    usr_name = models.CharField(max_length=200)

    def __str__(self):
        return (self.usr_id, self.usr_name)
    
class Habits(models.Model):
    hab_id     = models.IntegerField(default=0)
    hab_time   = models.DateTimeField('date published')
    hab_choice = models.CharField(max_length=200)

    def __str__(self):
        return (self.hab_id, self.hab_time, self.hab_choice)

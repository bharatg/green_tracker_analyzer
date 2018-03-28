from django.db import models

class Users(models.Model):
    usr_id = models.IntegerField(default=0)
    ust_name = models.CharField(max_length=200)

from django.db import models

class SimpleTable(models.Model):
    #text = models.CharField(max_length=200)
    usr_id = models.CharField(max_length=200)
    name   = models.CharField(max_length=200)

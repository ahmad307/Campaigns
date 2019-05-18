from django.db import models
from datetime import datetime


class Campaign(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    budget = models.IntegerField()
    goal = models.CharField(max_length=20)
    category = models.CharField(max_length=50)
    start_date = models.DateField(default=datetime.now())

    def __str__(self):
        return self.name

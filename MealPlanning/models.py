from django.db import models

# Create your models here.
class Meal(models.Model):
    date = models.DateField()
    meal = models.CharField(max_length=100)
    calID = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.calID} | {self.meal}"

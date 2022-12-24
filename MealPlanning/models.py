from django.db import models

# Create your models here.
class Meal(models.Model):
    eventID = models.CharField(primary_key=True, max_length=1000)
    date = models.DateField()
    meal = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.eventID} | {self.meal}"

from django.db import models


class Passenger(models.Model):
    id = models.IntegerField(primary_key=True)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    travelPoints = models.IntegerField()

    def __str__(self):
        return f'{self.id} {self.firstName} {self.lastName}'

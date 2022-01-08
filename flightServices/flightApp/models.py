from django.db import models

from django.db.models.signals import post_save  # señal que vamos a recibir
from django.dispatch import receiver   # es un decorador
from rest_framework.authtoken.models import Token   # es un model object
from django.conf import settings

class Flight(models.Model):
    flightNumber = models.CharField(max_length=10)
    operatingAirlines = models.CharField(max_length=20)
    departureCity = models.CharField(max_length=20)
    arrivalCity = models.CharField(max_length=20)
    dateOfDeparture = models.DateField()
    estimatedTimeOfDeparture = models.TimeField()

    def __str__(self):
        return f'{self.operatingAirlines}'


class Passenger(models.Model):
    firstName = models.CharField(max_length=20)
    middleName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.firstName} {self.lastName}'


class Reservation(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.flight} {self.passenger}'


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def createAuthToken(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)

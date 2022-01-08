from django.db import models


class Customer(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    phone = models.IntegerField()

    def __str__(self):
        return f'{self.firstName} {self.lastName}'


class Order(models.Model):
    product = models.CharField(max_length=20)
    quantity = models.CharField(max_length=10)
    customer = models.ForeignKey(Customer, related_name='orders', on_delete=models.CASCADE)

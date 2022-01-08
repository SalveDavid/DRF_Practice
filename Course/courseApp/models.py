from django.db import models


class Courses(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    ratings = models.IntegerField()

    def __str__(self):
        return f'{self.name} {self.description} {self.ratings}'

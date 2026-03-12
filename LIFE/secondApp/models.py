from django.db import models

# Create your models here.
class FieldRanger(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    location = models.CharField(max_length=200)
    allocatedAnimal = models.CharField(max_length=200)
    level = models.IntegerField()

    def __str__(self):
        return self.name


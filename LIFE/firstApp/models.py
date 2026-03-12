from django.db import models

# Create your models here.
class Animal(models.Model):
    # attributes
    name = models.CharField(max_length=200) 
    age = models.IntegerField()
    yob = models.IntegerField()
    current_weight = models.FloatField()
    image  = models.CharField(max_length =200)
    location = models.CharField(max_length= 200)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Plant(models.Model):
    name = models.CharField(max_length = 200)
    image = models.CharField(max_length = 200)
    location = models.CharField(max_length = 200)
    color = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


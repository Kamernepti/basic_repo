from django.db import models

class Dojos(models.Model):
    name = models.CharField(max_length= 255)
    city = models.CharField(max_length= 255)
    state = models.CharField(max_length= 2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Ninjas(models.Model):
    dojo = models.ForeignKey(Dojos, related_name="ninja", on_delete = models.CASCADE)
    first_name= models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
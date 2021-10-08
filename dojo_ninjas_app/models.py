from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Dojo(models.Model):
    name = models.CharField(max_length= 255)
    city = models.CharField(max_length= 255)
    state = models.CharField(max_length= 255)

class Ninja(models.Model):
    dojo = models.ForeignKey(Dojo, related_name="ninjas", on_delete = models.CASCADE)
    first_name = models.CharField(max_length= 255)
    last_name = models.CharField(max_length= 255)
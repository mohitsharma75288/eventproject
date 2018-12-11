from django.db import models

# Create your models here.
class book(models.Model):
	firstname=models.CharField(max_length=200)
	lastname=models.CharField(max_length=200)
	email=models.CharField(max_length=200)
	contact=models.CharField(max_length=200)


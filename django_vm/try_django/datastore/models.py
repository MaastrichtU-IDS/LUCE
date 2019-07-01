from django.db import models

# Create your models here.
class Dataset(models.Model):
	title 		= models.TextField()
	description = models.TextField(null=True, blank=True)
	owner 		= models.TextField()
	license 	= models.TextField()
	purpose 	= models.TextField(null=True)
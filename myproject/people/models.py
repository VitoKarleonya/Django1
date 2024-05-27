
from django.db import models
from django.db import models 


class Person(models.Model):
	surname = models.CharField(max_length=100)     
	name = models.CharField(max_length=100)     
	email = models.EmailField()     
	phone = models.CharField(max_length=20)      


	def __str__(self):
		return f'{self.surname} {self.name}'

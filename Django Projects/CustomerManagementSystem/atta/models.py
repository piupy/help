from django.db import models
from django.utils.timezone import now


# Create your models here.

class Customer(models.Model):
	sno = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50,default='')
	amount = models.FloatField(default=0)
	tran_date = models.DateTimeField(default=now)


	def __str__(self):
		return self.name

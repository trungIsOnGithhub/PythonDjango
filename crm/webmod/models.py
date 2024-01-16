from django.db import models

# Create your models here.
class Record(models.Model):
	first_name = models.CharField(max_length=68)
	last_name =  models.CharField(max_length=68)
	email =  models.CharField(max_length=100)
	phone = models.CharField(max_length=11)
	address =  models.CharField(max_length=100)
	city =  models.CharField(max_length=68)
	country =  models.CharField(max_length=68)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.email
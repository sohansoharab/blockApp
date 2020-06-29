from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.


class UserProfileInfo(models.Model):
	"""docstring for UserProfileInfo"""
	
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	# addition fields

	age = models.TextField()

	def __str__(self):
		return self.user.username
		
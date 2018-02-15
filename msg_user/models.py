from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class User(models.Model):
	first_name = models.CharField(max_length=40)
	last_name = models.CharField(max_length=40)
	city = models.CharField(max_length=40)
	email = models.EmailField(max_length=100)

	class Meta:
		verbose_name = "User"
		verbose_name_plural = "User"

	def __str__(self):
		return self.first_name


class Message(models.Model):
	message=models.CharField(max_length=140, null=True, blank=True)
	message_from = models.ForeignKey(User, related_name='message_from')
	message_to = models.ForeignKey(User, related_name='message_to')
 	created_on = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = "Message"
		verbose_name_plural = "Message"

	def __str__(self):
		return self.message


from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.
class Friend(models.Model):
	first_user_id = models.IntegerField()
	second_user_id = models.IntegerField()
	
	def second_user_name(self):
			return User.objects.get(id=self.second_user_id).username
	
class Friend_request(models.Model):
	sender_id = models.IntegerField()
	recipient_id = models.IntegerField()

	def sender_name(self):
		return User.objects.get(id=self.sender_id).username
		
	def recipient_name(self):
		return User.objects.get(id=self.recipient_id).username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	if created:
		Token.objects.create(user=instance)
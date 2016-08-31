from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils import timezone
from django.dispatch import receiver
from social.apps.django_app.default.models import UserSocialAuth


class User(AbstractUser):
	name = models.CharField(max_length=100, blank=True)
	paycheck = models.IntegerField(blank=True, default=10)

	def __str__(self):
		return self.username


class Team(models.Model):
	name = models.CharField(max_length=200)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


class Member(models.Model):
	team = models.ForeignKey('Team')
	user = models.ForeignKey('User')
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.user.username


class Work(models.Model):
	team = models.ForeignKey('Team')
	member = models.ForeignKey('User', on_delete=models.DO_NOTHING, related_name="works")
	period = models.ForeignKey('Period', default=0.5)

	date = models.DateField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.date)


class Period(models.Model):
	unit = models.FloatField(default=0.5)
	team = models.ForeignKey('Team')

	def __str__(self):
		return str(self.unit)

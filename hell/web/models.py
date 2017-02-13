from django.db import models
from django.utils import timezone
# Create your models here.



class Anounce(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	context = models.TextField()
	created = models.DateTimeField(default = timezone.now)
	published = models.DateTimeField(blank = True, null = True)

	def publish(self):
		self.published = timezone.now()
		self.save()

	def __str__(self):
		return self.title

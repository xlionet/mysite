from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Article(models.Model):
		title = models.CharField(max_length=200)
		pub_date = models.DateTimeField('date published')
		content = models.TextField()
		author = models.ForeignKey(User, on_delete=models.CASCADE)
	
		def __str__(self):
				return self.title
		def was_published_recently(self):
				now = timezone.now()
				return now -datetime.timedelta(days=1) <= self.pub_date <= now
				was_published_recently.admin_order_field = 'pub_date'
				was_published_recently.boolean = True
				was_published_recently.short_description = 'Published recently'
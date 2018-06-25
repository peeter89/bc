from django.db import models
from django.urls import reverse
from datetime import date, datetime
from django.utils import timezone

# Create your models here.


class Author(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	date_of_birth = models.DateField()
	description = models.TextField(max_length=2500)
	date_create = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ["last_name","first_name"]

	def publish_post_set(self):
		return self.post_set.filter(date_publish__lte=datetime.now())

	def get_absolute_url(self):
		return reverse('author-detail', args=[str(self.id)])

	def __str__(self):
		return '%s, %s' % (self.last_name, self.first_name)



class Hashtag(models.Model):
	name = models.CharField(max_length=50, unique=True, help_text="Hashtag name")
	author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
	date_create = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		ordering = ["name"]

	
	def publish_post_set(self):
		return self.post_set.filter(date_publish__lte=datetime.now())


	def get_absolute_url(self):
		return reverse('hashtag-detail', args=[str(self.id)])

	def __str__(self):
		return self.name



class Post(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField(max_length=250, null=True, blank=True)
	author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
	hashtag = models.ManyToManyField(Hashtag,help_text='Select a Hashtag for Post')
	date_create = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	date_publish = models.DateTimeField(default=timezone.now)


	@property
	def is_publish(self):
		if self.date_publish and timezone.now() >= self.date_publish:
			return True
		return False

	def display_hashtag(self):
        
		return ', '.join([ hashtag.name for hashtag in self.hashtag.all()[:5] ])
	display_hashtag.short_description = 'Hashtag'

	class Meta:
		ordering = ["-date_publish"]

	def get_absolute_url(self):
		return reverse('post-detail', args=[str(self.id)])

	def __str__(self):
		return self.name
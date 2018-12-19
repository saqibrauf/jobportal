from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils import timezone
from sorl.thumbnail import ImageField
from mptt.models import MPTTModel, TreeForeignKey


##################################################################################################################################
class Location(MPTTModel):
	name = models.CharField(max_length=70, unique=True)
	parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
	slug = models.SlugField(blank=True, editable=False)

	class MPTTMeta:
		order_insertion_by = ['name']

	class Meta:
		verbose_name_plural = 'Locations'
		ordering = ['name']

	def __str__(self):
		return self.name.title()

	def save(self, *args, **kwargs):
		self.name = self.name.title()
		self.slug = slugify(self.name)
		super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('location', args=[str(self.slug),])

##################################################################################################################################
class Category(MPTTModel):
	name = models.CharField(max_length=70, unique=True)
	parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
	slug = models.SlugField(blank=True, editable=False)
	
	class MPTTMeta:
		order_insertion_by = ['name']

	class Meta:
		verbose_name_plural = 'Categories'
		ordering = ['name']

	def __str__(self):
		return self.name.title()

	def save(self, *args, **kwargs):
		self.name = self.name.title()
		self.slug = slugify(self.name)
		super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('category', args=[str(self.slug),])

##################################################################################################################################
class Company(models.Model):
	user = models.ForeignKey(User, on_delete=None, blank=True, null=True, related_name='companies')
	name = models.CharField(max_length=75)
	slug = models.SlugField(max_length=80, blank=True, editable=False)
	logo = models.ImageField(upload_to='images/companies', blank=True)
	category = models.ManyToManyField(Category, blank=True, related_name='companies')
	website = models.URLField(max_length=255, blank=True)
	location = models.ManyToManyField(Location, related_name='companies', blank=True)
	info = models.TextField(blank=True)

	class Meta:
		verbose_name_plural = 'Companies'
		ordering = ['name']

	def __str__(self):
		return self.name.title()

	def save(self, *args, **kwargs):
		self.name = self.name.title()
		self.slug = slugify(self.name)
		if not self.user:
			self.user = User.objects.get(username='ourjobportal')
		super().save(*args, **kwargs)

##################################################################################################################################
class Job(models.Model):
	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255, blank=True, editable=False)
	desc = models.TextField(blank=True)
	GENDER = (
		('male', 'Male'),
		('female', 'Female')
	)
	gender = models.CharField(max_length=6, choices=GENDER, default='male')
	company = models.ForeignKey(Company, on_delete=None, blank=True, null=True, related_name='jobs')
	location = models.ForeignKey(Location, on_delete=None, blank=True, null=True, related_name='jobs')
	category = models.ForeignKey(Category, on_delete=None, blank=True, null=True, related_name='jobs')
	tags = TaggableManager(blank=True)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	job_url = models.URLField(max_length=255, blank=True)

	class Meta:
		verbose_name_plural = 'Jobs'
		ordering = ['-created_at']

	def __str__(self):
		return self.title.title()

	def save(self, *args, **kwargs):
		self.title = self.title.title()
		self.slug = slugify(self.title)
		super().save(*args, **kwargs)
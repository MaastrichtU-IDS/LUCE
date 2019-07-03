from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

User = settings.AUTH_USER_MODEL

class BlogPostManager(models.Manager):
	def published(self):
		now = timezone.now()
		# get_queryset == Blogpost.objects
		return self.get_queryset().filter(publish_date__lte=now)

class BlogPost(models.Model): # blogpost_set -> queryset
    # id = models.IntegerField() # pk
    user    = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title  = models.CharField(max_length=120)
    slug   = models.SlugField(unique=True) # hello world -> hello-world
    content  = models.TextField(null=True, blank=True)
    publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # This adds more methods to the objects attribute itself
    objects = BlogPostManager()
    # So Model Manager allows us to do BlogPost.objects.published()
    # It operates on ALL objects, whereas functions within BlogPost
    # class operate on ONE instance of class at a time

    class Meta:
    	# the `-` means that the MOST RECENT date will be first
    	ordering = ['-publish_date', '-updated', '-timestamp']
    	# this changes the order of the queryset & list view

    # object methods
    def get_absolute_url(self):
    	return f"/blog/{self.slug}"

    def get_edit_url(self):
    	return f"/blog/{self.slug}/edit"

    def get_delete_url(self):
    	return f"/blog/{self.slug}/delete"
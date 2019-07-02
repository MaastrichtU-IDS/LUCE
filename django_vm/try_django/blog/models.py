from django.db import models
from django.conf import settings

# Create your models here.

# This is how we obtain the user model of our site
# By obtaining it via settings is still works even if
# the user model implementation changes
User = settings.AUTH_USER_MODEL

class BlogPost(models.Model): #blogpost_set -> queryset
	user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL) 
	 # SET_NULL means it goes back to default (or null if no default exists) when user is deleted
	# user = models.ForeignKey(User, default=1, on_delete=models.CASCADE) 
	# CASCADE means if user is deleted his content/objects are deleted as well
	title = models.CharField(max_length=120)
	content = models.TextField(null=True, blank=True)
	slug = models.SlugField(unique=True) # hello world -> hello-world


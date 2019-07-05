from django.db import models

# Import user model
from django.conf import settings
User = settings.AUTH_USER_MODEL

# Module for combined queries
from django.db.models import Q

class Dataset(models.Model):
    title           = models.CharField(max_length=120)
    description     = models.TextField(null=True, blank=True)
    # file = models.FileField(upload_to='files/', blank=True, null=True)
    owner           = models.CharField(max_length=120) # owner name/institute
    owner_address   = models.CharField(max_length=180) # should be msg.sender
    license         = models.IntegerField() # encoded as integer
    
    # log user that uploaded the file
    created_by      = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    timestamp       = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)
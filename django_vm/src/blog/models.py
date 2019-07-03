from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

User = settings.AUTH_USER_MODEL

class BlogPostQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(publish_date__lte=now)

    def search(self, query):
        return self.filter(title__iexact=query)

class BlogPostManager(models.Manager):
    def get_queryset(self):
        return BlogPostQuerySet(self.model, using=self._db)
    # This allows us to do BP.objects.all().published()
    # So we have a custom filter
    # -> We need this for search & filtering

    def published(self):
        return self.get_queryset().published()
    # This allows to directly do BP.objects.published()

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().published().search(query)

class BlogPost(models.Model): # blogpost_set -> queryset
    # id = models.IntegerField() # pk
    user    = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    file = models.FileField(upload_to='files/', blank=True, null=True)
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
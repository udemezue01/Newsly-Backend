from django.db import models

# Create your models here.

class Tag(models.Model):

    title        = models.CharField(max_length=3000)

    slug         = models.SlugField(auto_created=True)


class Post(models.Model):

    user                  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

    title                 = models.CharField(max_length=3000, blank=True)
    content               = models.TextField(blank=True)
    tags                  = models.ManyToManyField()

    featured_Image        = models.FileField(blank=True)

    created_at            = models.DateTimeField(auto_now=True, auto_now_add=True)

    def __str__(self):
        return self.title

from __future__ import unicode_literals

from django.db import models


class Post(models.Model):

    title = models.CharField(max_length=100)
    body = models.TextField()

    published_at = models.DateTimeField(null=True)

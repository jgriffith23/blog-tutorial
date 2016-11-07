from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    """A model to represent blog posts."""

    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"pk": self.pk})

    # Both the Django girls tutorial and the official Django tutorial
    # have you make a __str__ instead of __repr__. Why...?
    def __str__(self):
        return "Title: %s, Author: %s" % (self.title, self.author)

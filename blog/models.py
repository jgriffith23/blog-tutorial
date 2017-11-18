from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    """A model to represent blog posts."""

    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    preview_graf = models.TextField(blank=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        """Sets a published date so that users can see the post."""

        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"pk": self.pk})

    def __str__(self):
        """How a post should be represented as a string."""

        return "Title: %s, Author: %s" % (self.title, self.author)


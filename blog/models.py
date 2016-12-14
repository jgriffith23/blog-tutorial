from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.urls import reverse
# from django_markup.fields import MarkupField


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
        """Sets a published date so that users can see the post."""

        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"pk": self.pk})

    def __str__(self):
        """How a post should be represented as a string."""

        return "Title: %s, Author: %s" % (self.title, self.author)

#FIXME: Consider making portfolio its own project
class Project(models.Model):
    """A model to represent project entries in a portfolio.

    I wonder, though--should this perhaps be a separate "app"? Or
    Is there enough overlap between this and a Post that there should be
    a mixin involved? Both should be published, and have title/text.
    """

    title = models.CharField(max_length=205)
    text = models.TextField()

    #FIXME: change field name
    image_url = models.ImageField(
        blank=True
    )

    github_url = models.URLField(
        blank=True
    )

    demo_url = models.URLField(
        blank=True
    )

    def get_absolute_url(self):
        return reverse("blog:project_detail", kwargs={"pk": self.pk})

    def __str__(self):
        """How a project should be represented as a string."""

        return self.title


from __future__ import unicode_literals

from django.db import models
from django.urls import reverse


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
    image = models.ImageField(
        upload_to="project-images",
        blank=True,
    )

    github_url = models.URLField(
        blank=True,
    )

    demo_url = models.URLField(
        blank=True,
    )

    def get_absolute_url(self):
        return reverse("portfolio:project_detail", kwargs={"pk": self.pk})

    def __str__(self):
        """How a project should be represented as a string."""

        return self.title

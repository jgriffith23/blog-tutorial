from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFill


class Project(models.Model):
    """A model to represent project entries in a portfolio."""

    title = models.CharField(max_length=205)
    text = models.TextField()

    image = ProcessedImageField(
        upload_to="static/portfolio/images",
        processors=[ResizeToFill(200,200)],
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

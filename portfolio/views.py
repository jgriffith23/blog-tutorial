from django.shortcuts import render

####################################
# Portfolio Projects
####################################
from django.views import generic
from portfolio.models import Project


class ProjectListView(generic.ListView):
    """List of all the projects. Ever."""

    template_name = "portfolio/project_list.html"
    queryset = Project.objects.order_by('title')

    context_object_name = "projects"


class ProjectDetailView(generic.DetailView):
    """Details about a single project.

    Includes full text, title, and optional image + external links.

    Shows option to edit when authenticated.
    """

    model = Project
    template_name = "portfolio/project_detail.html"

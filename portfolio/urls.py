from django.conf.urls import url, include
from . import views

app_name = 'portfolio'

urlpatterns = [
    url(r'^project', views.ProjectListView.as_view(), name='project_list'),
    url(r'^project/(?P<pk>\d+)/$', views.ProjectDetailView.as_view(), name='project_detail'),
    # url(r'^post/new/$', views.ProjectCreateView.as_view(), name='project_new'),
    # url(r'^post/(?P<pk>\d+)/edit$', views.ProjectUpdateView.as_view(), name='project_edit'),
]

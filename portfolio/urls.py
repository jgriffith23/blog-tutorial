from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.ProjectListView.as_view(), name='project_list'),
    url(r'^project/(?P<pk>\d+)/$', views.ProjectDetailView.as_view(), name='project_detail'),
    # url(r'^post/new/$', views.ProjectCreateView.as_view(), name='project_new'),
    # url(r'^post/(?P<pk>\d+)/edit$', views.ProjectUpdateView.as_view(), name='project_edit'),
    # url(r'^login/', views.LoginView.as_view(), name='login'),
    # url(r'^logout/', auth_views.logout, name='logout'),
]

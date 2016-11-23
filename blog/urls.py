from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^post/new/$', views.PostCreateView.as_view(), name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit$', views.PostUpdateView.as_view(), name='post_edit'),
    url(r'^login/', views.LoginView.as_view(), name='login'),
    url(r'^logout/', auth_views.logout, name='logout'),
]

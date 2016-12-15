from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import StaffuserRequiredMixin

from .models import Post
from .forms import PostForm

from django.views import generic
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm


####################################
# Authentication
####################################

class LoginView(generic.FormView):
    """A login page."""

    template_name = "blog/login.html"
    form_class = AuthenticationForm

    success_url = '/'

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)

####################################
# Posts
####################################

class PostListView(generic.ListView):
    """List of all posts...literally all of them ever."""

    template_name = "blog/post_list.html"
    queryset = Post.objects.order_by('-published_date')

    paginate_by = 5

    context_object_name = "posts"


class PostDetailView(generic.DetailView):
    """Details about a single post.

    Includes full text, pub date, and author.

    Shows option to edit when authenticated.
    """

    model = Post
    template_name = "blog/post_detail.html"


class PostCreateView(LoginRequiredMixin, StaffuserRequiredMixin, generic.CreateView):
    """Create a post."""

    login_url = '/login/'

    template_name = "blog/post_edit.html"
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.published_date = timezone.now()
        return super(PostCreateView, self).form_valid(form)


class PostUpdateView(LoginRequiredMixin, StaffuserRequiredMixin, generic.UpdateView):
    """Class for post update form."""

    login_url = '/login/'

    template_name = "blog/post_edit.html"
    form_class = PostForm

    def get_object(self, queryset=None):
        """Get the existing post record."""

        return get_object_or_404(Post, pk=self.kwargs["pk"])
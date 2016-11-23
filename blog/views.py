from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import StaffuserRequiredMixin

from .models import Post
from .forms import PostForm

from django.views import generic
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm


class LoginView(generic.FormView):
    """A login page."""

    template_name = "blog/login.html"
    form_class = AuthenticationForm

    success_url = '/'

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)


class PostListView(generic.ListView):
    """List of all posts...literally all of them ever."""

    template_name = "blog/post_list.html"
    queryset = Post.objects.order_by('-published_date')

    context_object_name = "posts"


class PostDetailView(generic.DetailView):
    """Details about a single post.

    Includes full text, pub date, and author.

    Shows option to edit when authenticated.
    """

    model = Post
    template_name = "blog/post_detail.html"


# FIXME: Give this class the ability to actually keep users out? R/n the template
# is actually doing the heavy lifting. Perhaps go back to method decorator
# from previous commit?
class PostCreateView(LoginRequiredMixin, StaffuserRequiredMixin, generic.CreateView):
    """Create a post."""

    # FIXME: Nononono. I can't keep this as admin. Build a login route.
    login_url = '/admin/'

    template_name = "blog/post_edit.html"
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super(PostCreateView, self).get_context_data(**kwargs)

        # FIXIME: Technically not using the context right now. Want to
        # be able to check it on base template somehow...?
        if self.request.user.is_staff:
            context['is_staff'] = True

        print "lalalala", context
        print self.request.user
        print context['is_staff']

        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.published_date = timezone.now()
        return super(PostCreateView, self).form_valid(form)


class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    """Class for post update form."""

    # FIXME: Nononono. I can't keep this as admin. Build a login route.
    login_url = '/admin/'

    template_name = "blog/post_edit.html"
    form_class = PostForm

    def get_object(self, queryset=None):
        """Get the existing post record."""
        return get_object_or_404(Post, pk=self.kwargs["pk"])

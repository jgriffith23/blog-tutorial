from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from braces.views import StaffuserRequiredMixin, LoginRequiredMixin
from .models import Post
from .forms import PostForm

from django.views import generic


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
class PostCreateView(generic.CreateView, StaffuserRequiredMixin, LoginRequiredMixin):
    """Create a post."""

    template_name = "blog/post_edit.html"
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.published_date = timezone.now()
        return super(PostCreateView, self).form_valid(form)

class PostUpdateView(generic.UpdateView):
    """Class for post update form."""

    template_name = "blog/post_edit.html"
    form_class = PostForm

    def get_object(self, queryset=None):
        """Get the existing post record."""
        return get_object_or_404(Post, pk=self.kwargs["pk"])

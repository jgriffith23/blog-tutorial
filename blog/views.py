from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
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


# FIXME: Do I need to create an account/login route...?
@method_decorator(login_required, name='dispatch')
class PostCreateView(generic.CreateView):
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

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

from django.views import generic

class PostListView(generic.ListView):
    """List of all posts...literally all of them ever."""

    template_name = "blog/post_list.html"
    queryset = (Post
                .objects
                .filter(published_date__lte=timezone.now())
                .order_by('-published_date')
               )

    context_object_name = "posts"

# class PostDetailView(generic.DetailView):
#     """Details about a single post.
#
#     Includes full text, pub date, and author.
#
#     Shows option to edit when authenticated.
#     """
#
#     template_name = "blog/post_detail.html"
#     context_object_name = "post"
#     queryset = Post.objects

    # def get(self, request):
    #     return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    #     return render(request, 'blog/post_list.html', {'posts': posts})


# def post_list(request):
#     """Display a list of all posts."""
#     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
#     return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    """Display text of a single post."""
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    """View post creation form and create new posts."""

    # FIXME: Break into "display" and "process" routes; this hurts. T.T
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # Create a new Post instance with the form data, set its author
            # and pub date, and commit it to the db.
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()

            # Take us to the post_detail page!
            return redirect('blog:post_detail', pk=post.pk)

    else:
        form = PostForm()

    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    """Edit an existing post."""

    # Try to fetch a post
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_detail', pk=post.pk)

    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_edit.html', {'form': form})



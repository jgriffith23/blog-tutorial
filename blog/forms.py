from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    """Create a form that makes blog posts easier to work with."""

    class Meta:
        model = Post
        fields = ('title', 'text',)

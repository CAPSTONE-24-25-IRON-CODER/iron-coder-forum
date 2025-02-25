from django import forms
from tinymce.widgets import TinyMCE
from .models import Post, Comment, Reply

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    class Meta:
        model = Post
        fields = ["title", "content", "categories", "tags"]

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 10}))
    class Meta:
        model = Comment
        fields = ["content"]

class ReplyForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 10}))
    class Meta:
        model = Reply
        fields = ["content"]


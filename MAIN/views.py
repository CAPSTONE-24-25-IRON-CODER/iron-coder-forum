from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm, CommentForm, ReplyForm

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comment_form = CommentForm()
    reply_form = ReplyForm()
    return render(request, 'detail.html', {
        'post': post,
        'comment_form': comment_form,
        'reply_form': reply_form,
    })

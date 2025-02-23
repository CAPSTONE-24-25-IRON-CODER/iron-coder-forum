from django.shortcuts import redirect, render, get_object_or_404
from .models import Author, Category, Post, Comment, Reply
from .utils import update_views
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
import os

def get_author(user):
    return Author.objects.get(user=user)

def home(request):
    forums = Category.objects.all()
    num_posts = Post.objects.all().count()
    num_users = User.objects.all().count()
    num_categories = forums.count()
    try:
        last_approved_post = Post.objects.filter(approved=True).latest("date")
    except:
        last_approved_post = []

    context = {
        "forums": forums,
        "num_posts": num_posts,
        "num_users": num_users,
        "num_categories": num_categories,
        "last_approved_post": last_approved_post,
        "title": "Home Page"
    }
    return render(request, "forums.html", context)

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    author = get_author(request.user) if request.user.is_authenticated else None

    if request.method == "POST":
        if "comment-form" in request.POST and not post.closed:
            comment = request.POST.get("comment")
            new_comment, created = Comment.objects.get_or_create(user=author, content=comment)
            post.comments.add(new_comment.id)
        elif "reply-form" in request.POST and not post.closed:
            reply = request.POST.get("reply")
            comment_id = request.POST.get("comment-id")
            comment_obj = Comment.objects.get(id=comment_id)
            new_reply, created = Reply.objects.get_or_create(user=author, content=reply)
            comment_obj.replies.add(new_reply.id)

    context = {
        "post": post,
        "title": post.title,
        "post_closed": post.closed,
    }
    update_views(request, post)
    return render(request, "detail.html", context)

def posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(approved=True, categories=category)
    paginator = Paginator(posts, 5)
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        "posts":posts,
        "forum": category,
        "title": "Posts"
    }

    return render(request, "posts.html", context)

@login_required
def create_post(request):
    context = {}
    form = PostForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            author = Author.objects.get(user=request.user)
            new_post = form.save(commit=False)
            new_post.user = author 
            new_post.save()
            form.save_m2m()
            return redirect("home")
    context.update({
        "form": form,
        "title": "Create New Post",
    })
    return render(request, "create_post.html", context)


def latest_posts(request):
    # posts = Post.objects.all().filter(approved=True)[:10]
    posts = Post.objects.order_by('-date')[:10]
    posts = Post.objects.filter(approved=True).order_by('-date')[:10]


    context = {
        "posts":posts,
        "title": "Latest 10 Posts"
    }

    return render(request, "latest-posts.html", context)

def search_result(request):
    query = request.GET.get('q')
    category = request.GET.get('category')
    if query:
        if category == "Titles":
            posts = Post.objects.filter(title__icontains=query, approved=True)
        elif category == "Descriptions":
            posts = Post.objects.filter(content__icontains=query, approved=True)
        else:  # Everything
            posts = Post.objects.filter((Q(title__icontains=query) | Q(content__icontains=query)), approved=True)
    else:
        posts = Post.objects.none()

    context = {
        "objects": posts,
        "query": query,
        "title": "Search Results"
    }

    return render(request, "search.html", context)


@csrf_exempt
def upload_image(request):
    if request.method == "POST" and request.FILES.get("file"):
        uploaded_file = request.FILES["file"]
        
        upload_folder = 'post-media/'
        
        file_path = os.path.join(upload_folder, uploaded_file.name)
        
        file_path = default_storage.save(file_path, uploaded_file)
        
        file_url = default_storage.url(file_path)
        
        return JsonResponse({"location": file_url})
    
    return JsonResponse({"error": "No file uploaded"}, status=400)
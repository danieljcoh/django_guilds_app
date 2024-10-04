from django.shortcuts import render
from django.http import HttpResponseNotFound
from .models import Post

# Create your views here.

def index(request):

    posts = Post.objects.all()

    return render(request, "guild_posts_app/index.html", {
        "all_posts": posts
    })

def post_details(request, post_id):

    try:
        specific_post = Post.objects.get(id=post_id)
    except:
        return HttpResponseNotFound("<h1>The Post is not found!</h1>")

    return render(request, "guild_posts_app/post_details.html", {
        "post": specific_post
    })
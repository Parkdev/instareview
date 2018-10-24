from django.shortcuts import render

# Create your views here.
from .models import Post


def post_list (request):
    posts = Post.objects.all()
    contest = {
        'posts' : posts,
    }
    return render(request, 'posts/posts_list.html',context)

from django.shortcuts import render, redirect

# Create your views here.
from members.models import User
from .forms import PostCreateForm
from .models import Post


def post_list (request):
    posts = Post.objects.all()
    context = {
        'posts' : posts,
    }
    return render(request, 'posts/post_list.html', context)

def post_create(request):

    if request.method == 'POST':
        post = Post(
            author=User.objects.first(),
            photo=request.FILES['photo'])
        post.save()
        return redirect('posts:post-list')
    else:
        form = PostCreateForm()
        context = {
            'form': form,
        }
        return render(request, 'posts/post_create.html', context)

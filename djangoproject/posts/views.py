from django.shortcuts import render
from django.http import HttpResponse

from .models import Posts

# Create your views here.
def index(request):
    #return HttpResponse('HELLO FROM POSTS')
    # bring the posts from the model
    posts = Posts.objects.all()[:10]
    # take this posts object and pass it in our template
    context = {
        'title' : 'Latest Posts',
        'posts' : posts
    }

    return render(request, 'posts/index.html', context)

def details(request, id):
    post = Posts.objects.get(id=id)

    context = {
        'post' : post,
    }

    return render(request, 'posts/details.html', context)
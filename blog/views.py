from django.shortcuts import render
from django.http import HttpResponse

from .models import Post


# Create your views here.
def index(request):
    posts= Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def article(request, id):
    post= Post.objects.get(id= id)
    tags= post.tags.split(',')
    return render(request, 'article.html', {'post': post, 'tags': tags})
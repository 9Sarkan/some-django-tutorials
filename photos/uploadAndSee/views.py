from django.shortcuts import render
from .models import Post
from django.shortcuts import render
from django.views import generic

def index(request):
    content = {
        'post' : Post.objects.all(),
    }
    return render(request, 'index.html', content)
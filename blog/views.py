from django.shortcuts import render
from .models import Post

def home(request):
    #  Context is a dictionary
    context = {
        'posts': Post.objects.all()
    }
    # Pass Dictionary into template to have access to it
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

from django.shortcuts import render, get_object_or_404
from .models import Post, Categorie
from django.http import HttpResponse


def index(request):
    return render(request, 'articles/post_list.html', {
        'categories': Categorie.objects.all(),
        'posts': Post.objects.all()[:5]
    })


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'articles/post_detail.html', {'post': post})

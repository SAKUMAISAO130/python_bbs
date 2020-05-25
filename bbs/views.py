from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article

def index(request):
    articles = Article.objects.all()
    context = {
        'message':'welcom my bbs',
        'articles':articles
    }
    return render(request, 'bbs/index.html', context)

def detail(request, id):
    article = get_object_or_404(Article, pk=id)
    context = {
        'message':'Detail',
        'article':article
    }
    return render(request, 'bbs/detail.html', context)

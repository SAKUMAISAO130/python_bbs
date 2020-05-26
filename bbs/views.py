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

def create(request):
    article = Article(content = 'そのまま入れる', user_name = 'taro')
    article.save()
    context = {
        'message':'Create',
        'article':article
    }
    return render(request, 'bbs/index.html', context)

def delete(request, id):
    article = get_object_or_404(Article, pk=id)
    article.delete()
    context = {
        'message':'Detail' + str(id),
        'article': article
    }
    return render(request, 'bbs/index.html', context)

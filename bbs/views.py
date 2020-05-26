from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article
from .forms import SearchForm
from .forms import ArticleForm

def index(request):
    searchForm = SearchForm(request.GET)
    if searchForm.is_valid():
        keyword = searchForm.cleaned_data['keyword']
        articles = Article.objects.filter(content__contains = keyword)
    else:
        searchForm = SearchForm()
        articles = Article.objects.all()

    context = {
        'message':'一覧を表示します。検索ボックスから検索できます',
        'articles':articles,
        'searchForm':searchForm
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
    if request.method == 'POST':
        articleFrom = ArticleForm(request.POST)
        if articleFrom.is_valid():
            article = articleFrom.save()

    context = {
        'message':'Create Article ' + str(article.id),
        'article':article
    }
    return render(request, 'bbs/detail.html', context)



def delete(request, id):
    article = get_object_or_404(Article, pk=id)
    article.delete()
    context = {
        'message':'Detail' + str(id),
        'article': article
    }
    return render(request, 'bbs/index.html', context)



def new(request):
    articleForm = ArticleForm()

    context = {
        'message':'新規作成',
        'articleForm': articleForm
    }

    return render(request, 'bbs/new.html', context)



def edit(request, id):
    article = get_object_or_404(Article, pk=id)
    articleForm = ArticleForm(instance=article)

    context = {
        'message':'Edit',
        'article':article,
        'articleForm': articleForm,
    }
    return render(request, 'bbs/edit.html', context)



def update(request, id):
    article = get_object_or_404(Article, pk=id)
    if request.method == 'POST':
        articleFrom = ArticleForm(request.POST, instance=article)
        if articleFrom.is_valid():
            article = articleFrom.save()

    context = {
        'message':'Create Article ' + str(article.id),
        'article':article
    }
    return render(request, 'bbs/detail.html', context)
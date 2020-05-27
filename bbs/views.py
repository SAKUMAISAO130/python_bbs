import logging

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Article
from .models import Comment
from .forms import SearchForm
from .forms import ArticleForm
from .forms import CommentForm

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
        'searchForm':searchForm,
    }
    return render(request, 'bbs/index.html', context)



def detail(request, id):
    article = get_object_or_404(Article, pk=id)

    comments = Comment.objects.all().filter(article_id = id)

    #
    # コメントフォーム
    #
    commentForm = CommentForm()

    context = {
        'message':'Detail',
        'article':article,
        'commentForm':commentForm,
        'comments':comments,
    }
    return render(request, 'bbs/detail.html', context)



def create(request):
    if request.method == 'POST':
        articleFrom = ArticleForm(request.POST)
        if articleFrom.is_valid():
            article = articleFrom.save()

    context = {
        'message':'Create Article ' + str(article.id),
        'article':article,
    }
    return render(request, 'bbs/detail.html', context)



def delete(request, id):
    article = get_object_or_404(Article, pk=id)
    article.delete()
    context = {
        'message':'Detail' + str(id),
        'article': article,
    }
    return render(request, 'bbs/index.html', context)



def new(request):
    articleForm = ArticleForm()

    context = {
        'message':'新規作成',
        'articleForm': articleForm,
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
        'article':article,
    }
    return render(request, 'bbs/detail.html', context)


def create_comment(request, id):
    
    if request.method == 'POST':

        commentForm = CommentForm(request.POST)

        if commentForm.is_valid():
            
            comment = Comment.objects.create(
                user_name = request.POST['user_name'],
                comment = request.POST['comment'],
                article_id = id
            )

    article = get_object_or_404(Article, pk=id)

    #
    # ログ出力
    #
    logger = logging.getLogger('development')
    logger.error(comment.id)

    context = {
        'message':'Create Comment ' + str(comment.id),
        'article':article,
    }

    return redirect('/bbs/' + str(id))

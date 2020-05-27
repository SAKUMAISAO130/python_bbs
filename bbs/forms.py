from django import forms
from .models import Article
from .models import Comment

class SearchForm(forms.Form):
    keyword = forms.CharField(label='タイトル検索', max_length=100)


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = (
            'content',
            'user_name',
            'category',
            'content_area',
            )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'user_name',
            'comment',
            )
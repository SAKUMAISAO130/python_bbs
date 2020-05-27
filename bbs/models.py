from django.db import models
from django.utils import timezone

class Article(models.Model):

    #
    # コンテンツ
    #
    content = models.CharField(
        max_length=200,
        null=True,
        )

    #
    # 名前
    #
    user_name = models.CharField(max_length=200, null = True)

    #
    # カテゴリ
    #
    category = models.IntegerField(
        verbose_name='',
        blank=True,
        null=True,
        default=0,
    )

    #
    # コンテンツエリア
    #
    content_area = models.TextField(
        verbose_name='',
        blank=True,
        null=True,
        max_length=1000,
    )

    def __str__(self):
        return self.content




class Comment(models.Model):

    #
    # Article ID
    #
    article_id = models.IntegerField(
        verbose_name='',
        blank=True,
        null=True,
        default=0,
    )

    #
    # 名前
    #
    user_name = models.CharField(max_length=200, null = True)


    #
    # コメント内容
    #
    comment = models.TextField(
        verbose_name='',
        blank=True,
        null=True,
        max_length=1000,
    )

    #
    # アップロード画像パス
    #
    image_path = models.TextField(
        verbose_name='',
        blank=True,
        null=True,
        max_length=1000,
    )

    def __str__(self):
        return self.content
from django.urls import path
from . import views

app_name = 'bbs'

urlpatterns = [
    #Index
    path('', views.index, name='index'),

    #Detail
    path('<int:id>', views.detail, name='detail'),

    #Create
    path('create', views.create, name='create'),

    #アクション　new
    path('new', views.new, name='new'),

    #Detail
    path('<int:id>/delete', views.delete, name='delete'),

    #Edit
    path('<int:id>/edit', views.edit, name='edit'),

    #アクション　update
    path('<int:id>/update', views.update, name='update'),

    #Create Comment
    path('<int:id>/create_comment', views.create_comment, name='create_comment'),

]
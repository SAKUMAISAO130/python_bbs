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

    #Detail
    path('<int:id>/delete', views.delete, name='delete'),

]
from django.contrib import admin
from django.urls import include,path
from django.views.generic import RedirectView

urlpatterns = [
    #TOPページ
    path('', RedirectView.as_view(url='/bbs/')),

    #BBS
    path('bbs/', include('bbs.urls')),

    #Admin
    path('admin/', admin.site.urls),    
]

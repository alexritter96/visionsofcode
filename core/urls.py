from django.urls import path

from . import views
from django.contrib.flatpages import views as flat_views


urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>', views.view_post, name='view_post'),
    path('about/', flat_views.flatpage, {'url': '/about/'}, name='about'),
    path('contact/', views.contact, name='contact')
]
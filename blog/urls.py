from django.urls import path

from . import views

app_name = "blogs"

urlpatterns = [
    path('', views.index, name= 'index'),
    path('posts/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('search/', views.search, name='search'),
]
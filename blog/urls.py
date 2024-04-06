from django.urls import path

from . import views

app_name = "blogs"

urlpatterns = [
    path('', views.IndexView.as_view(), name= 'index'),
    path('<int:blogid>/',views.get_BlogDetail, name='blogdetails'),
]
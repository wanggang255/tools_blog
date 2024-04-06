from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from .models import Blog

# Create your views here.
class IndexView(generic.ListView):
    template_name = "blog/index.html"
    context_object_name = "blog_latest_list"

    def get_queryset(self):
        return Blog.objects.order_by("-create_time")[:5]
    
def get_BlogDetail(request, blogid):
    blog = Blog.objects.get(id = blogid)
    return render(request, "blog/blogdetails.html",{"blog":blog})
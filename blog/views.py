from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from .models import Blog
from markdown import markdown
from django.template.defaultfilters import truncatechars_html
from django.shortcuts import render, get_object_or_404

def index(request):
    template_name = "blog/index.html"
    posts = Blog.objects.order_by("-create_time")[:5]
    # 渲染 Markdown 内容
    for post in posts:
        html_content = markdown(post.content)
        post.content = truncatechars_html(html_content, 100)
    return render(request, "blog/index.html", {"posts":posts})
    
def blog_detail(request, pk ):
    post = get_object_or_404(Blog, pk=pk)
    post.content = markdown(post.content)
    return render(request, "blog/blogdetails.html",{"post":post})

def search(request):
    query = request.GET.get('query')
    # 在这里执行搜索逻辑，根据查询词 'query' 进行过滤等操作
    # 获取相应的搜索结果
    # 将结果传递给模板进行渲染
    return render(request, 'search.html', {'query': query})
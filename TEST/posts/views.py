from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Post
import requests as req
# Create your views here.

def index(resquest):
    # posts = Post.objects.all()
    # SELECT * FROM posts_post
    # return render(resquest, "index.html", {"posts": posts})

    res = req.get("https://emma.pixnet.cc/mainpage/blog/categories/hot/28")

    articles = res.json()["articles"]

    return render(resquest, "index.html", {"articles": articles})

def index2(resquest):
    return HttpResponse('My Second Django APP')

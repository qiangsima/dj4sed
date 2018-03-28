from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from news.models import News


def detail(request, args):
    post = News.objects.all()[int(args)]
    str = 'timestamp=%s, total=%f, words=%s' % (post.timestamp, post.total, post.words)
    return HttpResponse(str)


def home(request):
    news_list = News.objects.all()
    return render(request, 'home.html', {'news_list': news_list})


from datetime import datetime

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect

# Create your views here.
from news.models import News


def detail(request, timestamp):
    try:
        news = News.objects.get(timestamp=str(timestamp))
        wordDict = {}
        arr = news.words[1:-1].split(', ')
        for word in arr:
            word = word.strip()
            if word:
                if word in wordDict:
                    wordDict[word] += 1
                else:
                    wordDict[word] = 1
        news.wordDict = wordDict
    except News.DoesNotExist:
        raise Http404
    return render(request, 'news.html', {'news': news})


def home(request):
    all_news = News.objects.all()
    paginator = Paginator(all_news, 10)
    page = request.GET.get('page')
    try:
        news_list = paginator.page(page)
    except PageNotAnInteger:
        news_list = paginator.page(1)
    except EmptyPage:
        news_list = paginator.paginator(paginator.num_pages)
    return render(request, 'home.html', {'news_list': news_list})


def news_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request, 'home.html')
        else:
            news_list = News.objects.filter(words__icontains=s)
            if len(news_list) == 0:
                return render(request, 'archives.html', {'news_list': news_list, 'error': True})
            else:
                return render(request, 'archives.html', {'news_list': news_list, 'error': False})
    return redirect('/')


def about_me(request):
    return render(request, 'aboutme.html')


def archives(request):
    try:
        news_list = News.objects.all()
    except News.DoesNotExist:
        raise Http404
    return render(request, 'archives.html', {'news_list': news_list, 'error': False})


def search_word(request, word):
    try:
        news_list = News.objects.filter(words_icontains=word)  # contains
    except News.DoesNotExist:
        raise Http404
    return render(request, 'tag.html', {'news_list': news_list})


def filter_total(request, total):
    all_news = News.objects.filter(total__gte=int(total))
    paginator = Paginator(all_news, 10)
    page = request.GET.get('page')
    try:
        news_list = paginator.page(page)
    except PageNotAnInteger:
        news_list = paginator.page(1)
    except EmptyPage:
        news_list = paginator.paginator(paginator.num_pages)
    return render(request, 'home.html', {'news_list': news_list})


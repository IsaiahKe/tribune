import datetime as dt
from django.shortcuts import redirect, render
from .models import Article
from django.http.response import Http404


def today_news(request):
    date=dt.date.today()
    news= Article.news_today()
    print(news)
    return render(request,'all-news/today_news.html',{"date":date,"news":news})

def past_days(request,pasttime):
    
    try:
        date=dt.datetime.strptime(pasttime,'%Y-%m-%d').date()
        
    except ValueError:
        raise Http404()
    if date== dt.date.today():
        return redirect(today_news())
    news=Article.pastdays_news(date)
    return render(request,'all-news/base.html',{"date":date,"news":news})

def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})
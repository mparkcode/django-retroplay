from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from django.core.paginator import Paginator
from .forms import CommentForm

# Create your views here.
def all_news(request):
    search_query = request.GET.get("query")
    if search_query:
        query = search_query
        return redirect('search_results', query)
    articles = Article.objects.all()
    paginator = Paginator(articles, 5)
    page = request.GET.get('page')
    articles=paginator.get_page(page)
    return render(request, "news/all_news.html", {'articles':articles})
    
def view_article(request, pk):
    if request.method=="POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.author=request.user
            article = Article.objects.get(pk=pk)
            comment.article=article
            comment.save()
            return redirect('view_article', article.id)
    search_query = request.GET.get("query")
    if search_query:
        query = search_query
        return redirect('search_results', query)
    article = Article.objects.get(pk=pk)
    comments = Comment.objects.filter(article = article)
    form = CommentForm()
    return render(request, "news/view_article.html", {'article':article, 'comments':comments, 'form':form})
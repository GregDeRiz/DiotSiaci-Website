from django.shortcuts import render
from .models import Article


# Create your views here.
def index(request):
    return render(request, 'index.html')


def blog(request):
    articles = Article.objects.all()
    return render(request, 'blog.html', {'articles': articles})

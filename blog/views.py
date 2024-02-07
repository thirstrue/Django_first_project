from django.shortcuts import render
from .models import *


# Create your views here.

def index(request):
    categories = Category.objects.all()
    articles = Article.objects.all()

    context = {
        'title': 'Главная страница',
        'articles': articles,
        'categories': categories
    }

    return render(request, 'main_page.html', context)

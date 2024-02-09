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


def category_page_view(request, category_id):
    articles = Article.objects.filter(category=category_id)

    trends = Article.objects.all().order_by('-views')

    context = {
        "title": f"Категория: {Category.objects.get(id=category_id).title}",
        "aritcles": articles,
        "trends": trends
    }

    return render(request, "category_page.html", context)
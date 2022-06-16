from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Article, Category

# Create your views here.


def home(request):
    article_list = Article.objects.published()
    paginator = Paginator(article_list, 3)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    context = {
        "articles": articles,
    }
    return render(request, "blog/home.html", context)


def detail(request, slug):
    context = {
        "article": get_object_or_404(Article.objects.published(), slug=slug),
    }
    return render(request, "blog/detail.html", context)


def category(request, slug):
    context = {
        "category": get_object_or_404(Category, slug=slug, status=True),
    }
    return render(request, "blog/category.html", context)


def api(request):
    data = {
        'title': 'مقاله اول',
        'id': 20,
        'slug': 'first-article'
    }
    return JsonResponse(data)

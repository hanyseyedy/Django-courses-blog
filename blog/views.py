from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Article, Category

# Create your views here.


def home(request):
    # return HttpResponse("hello world!")
    context = {
        "articles": Article.objects.filter(status='p'),
        "category": Category.objects.filter(status=True)
    }
    return render(request, "blog/home.html", context)


def detail(request, slug):
    context = {
        "article": get_object_or_404(Article, slug=slug)
    }
    return render(request, "blog/detail.html", context)


def api(request):
    data = {
        'title': 'مقاله اول',
        'id': 20,
        'slug': 'first-article'
    }
    return JsonResponse(data)

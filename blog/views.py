from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Articles

# Create your views here.


def home(request):
    # return HttpResponse("hello world!")
    context = {
        "articles": Articles.objects.filter(status='p').order_by('-publish')
    }
    return render(request, "blog/home.html", context)


def detail(request, slug):
    context = {
        "article": Articles.objects.get(slug=slug)
    }
    return render(request, "blog/single.html", context)


def api(request):
    data = {
        'title': 'مقاله اول',
        'id': 20,
        'slug': 'first-article'
    }
    return JsonResponse(data)

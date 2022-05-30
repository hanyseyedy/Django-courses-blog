from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse

# Create your views here.


def home(request):
    # return HttpResponse("hello world!")
    context = {
        'username': 'hany',
        'age': 37,
        'job': 'programer'
    }
    return render(request, "blog/home.html", context)


# def api(request):
#     data = {
#         'title': 'مقاله اول',
#         'id': 20,
#         'slug': 'first-article'
#     }
#     return JsonResponse(data)

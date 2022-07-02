from django.conf.urls.static import static
from django.conf import settings
from django.urls import URLPattern, path
from .views import ArticleList, AuthorList, api, ArticleDitail, CategoryList

app_name = "blog"
urlpatterns = [
    path('', ArticleList.as_view(), name="home"),
    path('page/<int:page>', ArticleList.as_view(), name="home"),
    path('article/<slug:slug>', ArticleDitail.as_view(), name="detail"),
    path('category/<slug:slug>', CategoryList.as_view(), name="category"),
    path('category/<slug:slug>/page/<int:page>',
         CategoryList.as_view(), name="category"),
    path('author/<slug:username>', AuthorList.as_view(), name="author"),
    path('author/<slug:username>/page/<int:page>',
         AuthorList.as_view(), name="author"),
    path('api', api, name="api")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

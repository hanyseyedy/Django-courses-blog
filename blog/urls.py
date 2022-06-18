from django.conf.urls.static import static
from django.conf import settings
from django.urls import URLPattern, path
from .views import home, api, detail, category

app_name = "blog"
urlpatterns = [
    path('', home, name="home"),
    path('page/<int:page>', home, name="home"),
    path('article/<slug:slug>', detail, name="detail"),
    path('category/<slug:slug>', category, name="category"),
    path('category/<slug:slug>/page/<int:page>', category, name="category"),
    path('api', api, name="api")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

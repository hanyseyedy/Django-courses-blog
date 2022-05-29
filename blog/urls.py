from django.conf.urls.static import static
from django.conf import settings
from django.urls import URLPattern, path
from .views import home, api

app_name = "blog"
urlpatterns = [
    path('', home, name="home"),
    path('api', api, name="api")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

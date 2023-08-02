from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('model', views.model_page, name='model')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)
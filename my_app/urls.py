from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('files/1/', Mar.as_view(), name='file1'),
    path('files/2/', Amal.as_view(), name='file2'),
    path('files/3/', Lab.as_view(), name='file3'),
    path('files/4/', Mus.as_view(), name='file4'),
    path('files/5/', Scop.as_view(), name='file5'),
    path('files/6/', Oak.as_view(), name='file6'),
    path('files/7/', Konf.as_view(), name='file7'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
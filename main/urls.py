from . import views
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .decorators import check_recaptcha

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.NotebookSList, name='NotebookSListByCategory'),
    url(r'^(?P<big_category_slug>[-\w]+)/(?P<category_slug>[-\w]+)/(?P<slug>[-\w]+)/$', check_recaptcha(views.ProductDetail), name='ProductDetail')
]

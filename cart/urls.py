from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^remove/(?P<product_slug>[-\w]+)/$', views.CartRemove, name='CartRemove'),
    url(r'^add/(?P<big_category_slug>[-\w]+)/(?P<slug>[-\w]+)/', views.CartAdd, name='CartAdd'),
    url(r'^versus/remove/(?P<product_slug>[-\w]+)/$', views.VersusRemove, name='VersusRemove'),
    url(r'^versus/add/(?P<big_category_slug>[-\w]+)/(?P<slug>[-\w]+)/', views.VersusAdd, name='VersusAdd'),
    url(r'^versus/$', views.VersusDetail, name='VersusDetail'),
    url(r'^craft/remove/(?P<big_category_slug>[-\w]+)/(?P<product_slug>[-\w]+)/$', views.CraftRemove, name='CraftRemove'),
    url(r'^craft/add/(?P<big_category_slug>[-\w]+)/(?P<category_slug>[-\w]+)/(?P<slug>[-\w]+)/', views.CraftAdd, name='CraftAdd'),
    url(r'^craft/$', views.CraftDetail, name='CraftDetail'),
    url(r'^$', views.CartDetail, name='CartDetail')


]

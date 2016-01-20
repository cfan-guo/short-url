from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^$', views.success, name='success'),
  url(r'(?P<short_url>)/$', views.short, name='short')
]

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='articles'),
    url(r'^(?P<slug>[\w-]+)/$', views.post_detail, name='post_detail'),
]

from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailArticle.as_view(), name='detail'),
    url(r'^send-article/$', views.post_article, name='post'),
]
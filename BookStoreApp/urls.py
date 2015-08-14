from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^book/(?P<book_id>[0-9]+)/$', views.book_detail, name='bookdetail'),
    url(r'^author/(?P<author_id>[0-9]+)/$', views.author_detail, name='authordetail'),
    url(r'^book/(?P<book_id>[0-9]+)/review/$', views.book_review, name='bookreview'),
]
from django.conf.urls import url

from . import views

urlpatterns = [
    #  The '$' is an end of string match character, that chops off the rest
    #  of url and sends it to URLconf for more processing
    # /BookStoreApp/
    url(r'^$', views.index, name='index'),
    # /BookStoreApp/2/
    url(r'^(?P<book_id>[0-9]+)/$', views.detail, name='detail'),
    # /BookStoreApp/1/results/$
    url(r'^(?P<book_id>[0-9]+)/results/$', views.results, name='results'),
    # BookStoreApp/3/vote/$
    url(r'^(?P<book_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
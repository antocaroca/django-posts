from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    
    url(r'^details/(?P<id>\d+)/$', views.index, name='details')
]
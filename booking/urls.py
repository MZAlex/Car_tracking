from django.conf.urls import url
from . import views
from views import create_account

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create_account/$', create_account),
]
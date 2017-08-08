from django.conf.urls import url
from . import views
from views import create_account, retreive, my_reservations
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create_account/$', create_account),
    url(r'^book/$', retreive, name='retreive'),
    url(r'^my_reservations/$', my_reservations),
]
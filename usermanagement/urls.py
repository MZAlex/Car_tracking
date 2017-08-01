from django.conf.urls import include, url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^success/$', TemplateView.as_view(template_name="user/success.html")),
]
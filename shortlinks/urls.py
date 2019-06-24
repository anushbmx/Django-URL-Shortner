from django.conf.urls import url
from shortlinks import views

urlpatterns = [
    url(r'^(?P<id>[a-zA-Z0-9]+)$', views.link, name='shortlink.index'),
]

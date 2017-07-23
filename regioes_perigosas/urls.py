from django.conf.urls import url
from regioes_perigosas import views

urlpatterns = [
    url(r'^regioes_perigosas/$', views.regioes_perigosas),
]

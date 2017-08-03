from django.conf.urls import url
from ocorrencia_classificador import views

urlpatterns = [
    url(r'^ocorrencia_classificador/$', views.ocorrencia_classificador),
]

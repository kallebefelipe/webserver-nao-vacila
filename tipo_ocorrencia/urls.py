from django.conf.urls import url
from tipo_ocorrencia import views

urlpatterns = [
    url(r'^tipo_ocorrencia/$', views.tipo_ocorrencia),
]

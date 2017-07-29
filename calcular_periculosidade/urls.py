from django.conf.urls import url
from calcular_periculosidade import views

urlpatterns = [
    url(r'^calcular_periculosidade/$', views.calcular_periculosidade),
]

from django.conf.urls import url
from estatisticas import views

urlpatterns = [
    url(r'^estatisticas/$', views.estatisticas),
]

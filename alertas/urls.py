from django.conf.urls import url
from alertas import views

urlpatterns = [
    url(r'^alertas/$', views.alertas),
]

from django.conf.urls import url
from gerar_rota import views

urlpatterns = [
    # url(r'^gerar_rota/(?P<latitude_origem>\w{0,50})/(?P<longitude_origem>\w{0,50})/(?P<latitude_destino>\w{0,50})/(?P<longitude_destino>\w{0,50})/$',
    #     views.gerar_rota),
    url(r'^gerar_rota/$', views.gerar_rota),
]

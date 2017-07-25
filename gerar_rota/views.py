# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.decorators import api_view
from rest_framework.response import Response
from gerar_rota.load import LoadToPostgres


@api_view(['GET'])
def gerar_rota(request):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        latitude_origem = request.GET['latitude_origem']
        longitude_origem = request.GET['longitude_origem']
        latitude_destino = request.GET['latitude_destino']
        longitude_destino = request.GET['longitude_destino']
        load = LoadToPostgres()
        data = load.get(latitude_origem, longitude_origem, latitude_destino,
                        longitude_destino)
        return Response(data)

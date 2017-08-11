# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from alertas.load import LoadToPostgres


@api_view(['GET', 'POST', 'DELETE'])
def alertas(request):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        try:
            id_usuario = request.GET['id_usuario']
            load = LoadToPostgres()
            data = load.get_by_user(id_usuario)
            return Response(data)
        except:
            pass
        load = LoadToPostgres()
        data = load.get_all()
        return Response(data)

    elif request.method == 'POST':
        try:
            load = LoadToPostgres(request.data)
            data = load.add()
            return Response(data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    # elif request.method == 'DELETE':
    #     snippets.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

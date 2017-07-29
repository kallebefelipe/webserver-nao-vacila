# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.decorators import api_view
from rest_framework.response import Response
from calcular_periculosidade.load import LoadToPostgres


@api_view(['PUT'])
def calcular_periculosidade(request):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'PUT':
        load = LoadToPostgres()
        data = load.get(request.data)
        return Response(data)

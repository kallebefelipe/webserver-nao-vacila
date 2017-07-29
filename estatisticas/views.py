# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.decorators import api_view
from rest_framework.response import Response
from estatisticas.load import LoadToPostgres


@api_view(['GET'])
def estatisticas(request):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        load = LoadToPostgres()
        data = load.get_estatisticas()
        return Response(data)

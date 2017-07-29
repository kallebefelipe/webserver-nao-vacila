# -*- coding: utf-8 -*-

from regioes_perigosas.models import RegiaoPerigosa
from nao_vacila.base import Base
from math import sin, cos, sqrt, atan2, radians
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class PostgresConnection(object):

    postgresql_database_url = 'postgres://wjrcqlhxqdotyk:b94941094d4ecbac5b9beae6901a886a28bcdccebf5bb60ed8214d04bfb657fa@ec2-107-20-186-238.compute-1.amazonaws.com:5432/d3fkknhsaktvl8'

    def __init__(self):
        self.engine = self.get_engine()
        self.create_tables()
        self.Session = sessionmaker(bind=self.engine)

    def create_connection(self):
        return self.Session()

    def create_tables(self):
        Base.metadata.create_all(self.engine)

    def get_engine(self):
        return create_engine(self.postgresql_database_url)


class LoadToPostgres(PostgresConnection):

    """docstring for LoadToPostgres"""

    def distancia(self, lat1, lon1, lat2, lon2):
        R = 6373.0

        lat1 = radians(lat1)
        lon1 = radians(lon1)
        lat2 = radians(lat2)
        lon2 = radians(lon2)

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c

        return distance

    def lugar_perigoso(self, regioes_perigosas, ponto):
        for each in regioes_perigosas:
            data = each.__dict__
            dist = self.distancia(data['latitude'], data['longitude'],
                                  ponto['lat'], ponto['lng'])
            if dist < 0.5:
                return True
        return False

    def get(self, rotas):
        session = self.create_connection()
        regioes_perigosas = session.query(RegiaoPerigosa).all()
        # rotas_dict = rotas.json()
        for rota in rotas['routes']:
            contagem_lugar_perigoso = 0
            for caminho in rota['legs'][0]['steps']:
                start = caminho['start_location'] # lat e lng
                end = caminho['end_location']
                if self.lugar_perigoso(regioes_perigosas, start) or self.lugar_perigoso(regioes_perigosas, end):
                    contagem_lugar_perigoso += 1
            rota['regioes_perigosas'] = contagem_lugar_perigoso
        return rotas

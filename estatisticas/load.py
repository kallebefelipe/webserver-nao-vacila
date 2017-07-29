# -*- coding: utf-8 -*-

from regioes_perigosas.models import RegiaoPerigosa
from nao_vacila.base import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ocorrencia.models import Ocorrencia
from sqlalchemy import func


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

    def get_estatisticas(self):
        session = self.create_connection()
        count2 = (func.count(Ocorrencia.bairro)).label('count2')
        distribuicao_bairro = session.query(Ocorrencia.bairro, count2).\
            group_by(Ocorrencia.bairro).all()
        distribuicao = []
        for bairo, qt   in distribuicao_bairro:
            distribuicao.append({bairo: qt})
        return distribuicao

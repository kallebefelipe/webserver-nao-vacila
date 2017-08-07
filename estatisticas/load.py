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
        estatisticas = {}
        session = self.create_connection()
        count2 = (func.count(Ocorrencia.bairro)).label('count2')
        distribuicao = session.query(Ocorrencia.bairro, count2).\
            group_by(Ocorrencia.bairro).all()
        distribuicao_bairro = []
        for bairro, qt in distribuicao:
            if bairro is not None:
                if 'rua' not in bairro and 'avenida' not in bairro and bairro != '?':
                    distribuicao_bairro.append({'bairro': bairro, 'quantidade': qt})
        estatisticas['distribuicao_bairro'] = distribuicao_bairro

        count2 = (func.count(Ocorrencia.id_tipo)).label('count2')
        distribuicao = session.query(Ocorrencia.id_tipo, count2).\
            group_by(Ocorrencia.id_tipo).all()
        distribuicao_tipo = []
        for tipo, qt in distribuicao:
            if tipo is not None:
                if str(tipo).isdigit():
                    tipo_oco = None

                    if int(tipo) == 1:
                        tipo_oco = 'assalto'
                    elif int(tipo) == 2:
                        tipo_oco = 'roubo'
                    elif int(tipo) == 3:
                        tipo_oco = 'sequestro'
                    elif int(tipo) == 4:
                        tipo_oco = 'arrombamento'
                    elif int(tipo) == 5:
                        tipo_oco = 'tiroteio'
                    elif int(tipo) == 6:
                        tipo_oco = 'homicidio'
                    elif int(tipo) == 7:
                        tipo_oco = 'trafico'
                    elif int(tipo) == 8:
                        tipo_oco = 'agressao'
                    elif int(tipo) == 9:
                        tipo_oco = 'estupro'
                    elif int(tipo) == 10:
                        tipo_oco = 'acidente'
                    if tipo_oco is not None:
                        distribuicao_tipo.append({'tipo': tipo_oco, 'quantidade': qt})

        estatisticas['distribuicao_tipo'] = distribuicao_tipo

        distribuicao = session.query(Ocorrencia.data).all()
        distribuicao_ano = []
        dict_distri_ano = {}
        for ano in distribuicao:
            ano = ano[0]
            if ano is not None:
                if ano.strip != '':
                    valido = False
                    if '-' in ano:
                        ano = ano.split('-')[0]
                        valido = True
                    elif '/' in ano:
                        ano = ano.split('/')[2]
                        valido = True
                    if valido:
                        if ano not in dict_distri_ano:
                            dict_distri_ano[ano] = 0
                        else:
                            dict_distri_ano[ano] += 1
        for each in dict_distri_ano.keys():
            distribuicao_ano.append({'ano': each, 'quantidade': dict_distri_ano[each]})

        estatisticas['distribuicao_ano'] = distribuicao_ano

        return estatisticas

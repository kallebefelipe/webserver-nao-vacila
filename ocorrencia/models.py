# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Ocorrencia(Base):

    __tablename__ = 'ocorrencia'

    id = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(String, nullable=True)
    hora = Column(String, nullable=True)
    titulo = Column(String, nullable=True)
    id_usuario = Column(String, nullable=True)
    latitude = Column(String, nullable=True)
    longitude = Column(String, nullable=True)
    descricao = Column(String, nullable=True)
    id_tipo = Column(String, nullable=True)
    endereco_rua = Column(String, nullable=True)

    def __init__(self, row):
        if 'data' in row:
            self.descricao = row['data']
        if 'hora' in row:
            self.hora = row['hora']
        if 'titulo' in row:
            self.titulo = row['titulo']
        if 'id_usuario' in row:
            self.id_usuario = row['id_usuario']
        if 'longitude' in row:
            self.longitude = row['longitude']
        if 'descricao' in row:
            self.descricao = row['descricao']
        if 'id_tipo' in row:
            self.id_tipo = row['id_tipo']
        if 'endereco_rua' in row:
            self.endereco_rua = row['endereco_rua']

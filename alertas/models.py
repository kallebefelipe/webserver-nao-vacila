# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from nao_vacila.base import Base


class Alerta(Base):

    __tablename__ = 'alerta'

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String, nullable=True)
    endereco = Column(String, nullable=True)
    id_usuario = Column(String, nullable=True)
    token = Column(String, nullable=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    raio = Column(Integer, nullable=True)

    def __init__(self, row):
        if 'titulo' in row:
            self.titulo = row['titulo']
        if 'endereco' in row:
            self.endereco = row['endereco']
        if 'id_usuario' in row:
            self.id_usuario = row['id_usuario']
        if 'latitude' in row:
            self.latitude = row['latitude']
        if 'longitude' in row:
            self.longitude = row['longitude']
        if 'token' in row:
            self.token = row['token']
        if 'raio' in row:
            self.raio = int(row['raio'])

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from nao_vacila.base import Base


class Usuario(Base):

    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(String, nullable=True)
    token = Column(String, nullable=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    raio = Column(String, nullable=True)

    def __init__(self, row):
        if 'id_usuario' in row:
            self.id_usuario = row['id_usuario']
        if 'token' in row:
            self.token = row['token']
        if 'latitude' in row:
            self.latitude = row['latitude']
        if 'longitude' in row:
            self.longitude = row['longitude']
        if 'token' in row:
            self.token = row['token']

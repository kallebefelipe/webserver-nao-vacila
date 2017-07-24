# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from nao_vacila.base import Base
import unicodedata


class Ocorrencia(Base):

    __tablename__ = 'ocorrencia'

    id = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(String, nullable=True)
    hora = Column(String, nullable=True)
    titulo = Column(String, nullable=True)
    id_usuario = Column(String, nullable=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    descricao = Column(String, nullable=True)
    id_tipo = Column(String, nullable=True)
    endereco = Column(String, nullable=True)
    bairro = Column(String, nullable=True)

    def normalize_ascii(self, value):
        return unicodedata.normalize('NFKD', value) \
            .encode('ascii', 'ignore')

    def normalize_string(self, value):
        return str(self.normalize_ascii(value))[2:-1].strip()

    def __init__(self, row):
        if 'data' in row:
            self.data = row['data']
        if 'hora' in row:
            self.hora = row['hora']
        if 'titulo' in row:
            self.titulo = row['titulo']
        if 'id_usuario' in row:
            self.id_usuario = row['id_usuario']
        if 'longitude' in row:
            self.longitude = row['longitude']
        if 'latitude' in row:
            self.latitude = row['latitude']
        if 'descricao' in row:
            self.descricao = row['descricao']
        if 'id_tipo' in row:
            self.id_tipo = row['id_tipo']
        if 'endereco' in row:
            self.endereco = row['endereco']
        if 'bairro' in row:
            self.bairro = self.normalize_string(str(row['bairro'])).lower()

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from nao_vacila.base import Base


class TipoOcorrencia(Base):

    __tablename__ = 'tipo_ocorrencia'

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String, nullable=True)
    tipo = Column(String, nullable=True)
    url_imagem = Column(String, nullable=True)

    def __init__(self, row):
        if 'titulo' in row:
            self.titulo = row['titulo']
        if 'tipo' in row:
            self.tipo = row['tipo']
        if 'url_imagem' in row:
            self.url_imagem = row['url_imagem']

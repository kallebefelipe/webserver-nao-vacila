# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from nao_vacila.base import Base


class Usuario(Base):

    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=True)
    sexo = Column(String, nullable=True)
    cidade = Column(String, nullable=True)
    email = Column(String, nullable=True)
    id_fb = Column(String, nullable=True)
    id_google = Column(String, nullable=True)
    url_foto = Column(String, nullable=True)

    def __init__(self, row):
        if 'nome' in row:
            self.nome = row['nome']
        if 'sexo' in row:
            self.sexo = row['sexo']
        if 'cidade' in row:
            self.cidade = row['cidade']
        if 'email' in row:
            self.email = row['email']
        if 'id_fb' in row:
            self.id_fb = row['id_fb']
        if 'id_google' in row:
            self.id_google = row['id_google']
        if 'url_foto' in row:
            self.url_foto = row['url_foto']

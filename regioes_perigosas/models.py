# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from nao_vacila.base import Base


class RegiaoPergigosa(Base):

    __tablename__ = 'regiao_perigosa'

    id = Column(Integer, primary_key=True, autoincrement=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    def __init__(self, row):
        if 'latitude' in row:
            self.latitude = float(row['latitude'])
        if 'longitude' in row:
            self.longitude = float(row['longitude'])

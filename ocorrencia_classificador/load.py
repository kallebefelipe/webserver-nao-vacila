# -*- coding: utf-8 -*-

from ocorrencia.models import Ocorrencia
from ocorrencia.models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_
import requests


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

    def __init__(self, row=None):
        super(LoadToPostgres, self).__init__()
        self.row = row
        self.elements = []

    def rows_to_models(self):
        elemento = Ocorrencia(self.row)
        self.elements.append(elemento)

    def save_models(self):

        session = self.create_connection()
        for el in self.elements:
            try:
                session.add(el)
            except:
                session.rollback()
                raise Exception('Elemento nao salvo: %s' % el)
        try:
            session.commit()
        except:
            session.rollback()
            raise Exception('Elemento nao salvo: %s' % el)
        finally:
            session.close()
        session.close()

    def get_coordenadas(self):
        if 'endereco' in self.row:
            response = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address="+self.row['endereco'])
        if response:
            for each in response.json()['results']:
                if 'PE' in each['formatted_address']:
                    longitude = each['geometry']['location']['lng']
                    latitude = each['geometry']['location']['lat']
                    endereco_encontradao = True
                    return latitude, longitude

    def add(self):
        result = []
        session = self.create_connection()
        if 'data' in self.row and 'hora' in self.row:
            result = session.query(Ocorrencia).\
                filter(and_(Ocorrencia.data==self.row['data'], Ocorrencia.hora==self.row['hora'])).all()

        if len(result) == 0:
            latitude, longitude =  self.get_coordenadas()
            if latitude is not None and longitude is not None:
                self.row['latitude'] = latitude
                self.row['longitude'] = longitude
                self.rows_to_models()
                self.save_models()

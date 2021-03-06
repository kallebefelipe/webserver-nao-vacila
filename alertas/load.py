# -*- coding: utf-8 -*-

from .models import Alerta
from .models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from push_notifications.models import GCMDevice


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
        elemento = Alerta(self.row)
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

    def add(self):
        self.rows_to_models()
        self.save_models()

    def get_all(self):
        session = self.create_connection()

        result = session.query(Alerta).all()
        data = []
        for each in result:
            linha = each.__dict__
            linha.pop('_sa_instance_state', None)
            data.append(linha)
        return data

    def get_by_user(self, id_usuario):

        session = self.create_connection()

        result = session.query(Alerta).filter(Alerta.id==int(id_usuario)).all()

        data = []
        for each in result:
            linha = each.__dict__
            linha.pop('_sa_instance_state', None)
            data.append(linha)
        return data

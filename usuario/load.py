# -*- coding: utf-8 -*-

from .models import Usuario
from .models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


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
        elemento = Usuario(self.row)
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
        session = self.create_connection()
        nao_vacila_id = {}
        if 'id_fb' in self.row:
            if self.row['id_fb'] is not None:
                result = session.query(Usuario).filter_by(id_fb=self.row['id_fb'])
                for each in result:
                    linha = each.__dict__
                    nao_vacila_id['nao_vacila_id'] = linha['id']
                    return nao_vacila_id
        elif 'id_google' in self.row:
            if self.row['id_google'] is not None:
                result = session.query(Usuario).filter_by(id_fb=self.row['id_fb'])
                if len(result) > 0:
                    for each in result:
                        linha = each.__dict__
                        nao_vacila_id['nao_vacila_id'] = linha['id']
                        return nao_vacila_id
        self.rows_to_models()
        self.save_models()

        if 'id_fb' in self.row:
            if self.row['id_fb'] is not None:
                result = session.query(Usuario).filter_by(id_fb=self.row['id_fb'])
                for each in result:
                    linha = each.__dict__
                    nao_vacila_id['nao_vacila_id'] = linha['id']
                    return nao_vacila_id
        elif 'id_google' in self.row:
            if self.row['id_google'] is not None:
                result = session.query(Usuario).filter_by(id_fb=self.row['id_fb'])
                if len(result) > 0:
                    for each in result:
                        linha = each.__dict__
                        nao_vacila_id['nao_vacila_id'] = linha['id']
                        return nao_vacila_id

    def get_all(self):
        session = self.create_connection()

        result = session.query(Usuario).all()
        data = []
        for each in result:
            linha = each.__dict__
            linha.pop('_sa_instance_state', None)
            data.append(linha)
        return data

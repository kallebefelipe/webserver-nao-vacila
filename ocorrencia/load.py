# -*- coding: utf-8 -*-

from .models import Ocorrencia
from usuario.models import Usuario
from tipo_ocorrencia.models import TipoOcorrencia
from push_notifications.models import GCMDevice
from math import sin, cos, sqrt, atan2, radians
from alertas.models import Alerta
# from alertas.models import TipoOcorrencia
from .models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date

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

    def enviar_mensagem(self, alerta):
        session = self.create_connection()
        result = session.query(Usuario).filter(Usuario.id_usuario==alerta['token']).all()
        for each in result:
            linha = each.__dict__
            fcm_device = \
                GCMDevice.objects.create(registration_id=linha['token'],
                                         cloud_message_type="FCM",
                                         )
            fcm_device.send_message(self.row)

    def distancia(self, lat1, lon1, lat2, lon2):
        R = 6373.0

        lat1 = radians(lat1)
        lon1 = radians(lon1)
        lat2 = radians(lat2)
        lon2 = radians(lon2)

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c

        return distance

    def verificar_raio(self, alerta):
        if self.distancia(self.row['latitude'], self.row['longitude'],
                          alerta['latitude'], alerta['longitude']) < \
            alerta['raio']:
            self.enviar_mensagem(alerta)

    def verificar_alerta(self):
        session = self.create_connection()
        result = session.query(Alerta).all()

        for each in result:
            alerta = each.__dict__
            self.verificar_raio(alerta)

    def add(self):
        try:
            self.verificar_alerta()
        except:
            pass
        self.rows_to_models()
        self.save_models()

    def get_all(self):
        session = self.create_connection()

        result = session.query(Ocorrencia).all()

        ocorrencias = []

        for each in result:
            linha = each.__dict__
            dt = date.today()
            if (str(dt.year) in str(linha['data'])) or (str(dt.year - 1) in str(linha['data'])):
                ocorrencias.append(each)
        data = []
        for each in ocorrencias:
            linha = each.__dict__
            if 'id_tipo' in linha:
                tipo_ocorrencia = session.query(TipoOcorrencia).all()
                if tipo_ocorrencia:
                    linha['tipo_ocorrencia'] = tipo_ocorrencia[0].__dict__
            linha.pop('_sa_instance_state', None)
            data.append(linha)
        return data

    def get_by_user(self, id_usuario):
        session = self.create_connection()
        result = session.query(Ocorrencia).filter(Ocorrencia.id==int(id_usuario)).all()

        data = []
        for each in result:
            linha = each.__dict__
            if 'id_tipo' in linha:
                tipo_ocorrencia = session.query(TipoOcorrencia).all()
                if tipo_ocorrencia:
                    linha['tipo_ocorrencia'] = tipo_ocorrencia[0].__dict__
            linha.pop('_sa_instance_state', None)
            data.append(linha)
        return data

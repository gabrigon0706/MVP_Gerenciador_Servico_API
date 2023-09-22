from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base


class Chamado(Base):
    __tablename__ = 'Chamado'

    id = Column("pk_chamado", Integer, primary_key=True)
    nome = Column(String(140))
    descricao = Column(String(140))
    prioridade = Column(String(50))
    data_insercao = Column(DateTime, default=datetime.now())


    def __init__(self, nome:str, descricao:str, prioridade:int,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Chamado

        Arguments:
            nome: nome do solicitante.
            descricao: descricao da requisicao
            prioridade: prioridade
            data_insercao: data de quando foi criado chamado na base
        """

        self.nome = nome
        self.descricao = descricao
        self.prioridade = prioridade

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao

 

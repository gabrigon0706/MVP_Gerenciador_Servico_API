from pydantic import BaseModel
from typing import Optional, List
from model.chamado import Chamado




class ChamadoSchema(BaseModel):
    """ Define como um novo chamado a ser inserido deve ser representado
    """
    nome: str = "Gabriel"
    descricao: Optional[str] = "Descrever seu pedido"
    prioridade: str = "Medio"


class ChamadoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no id do chamado.
    """
    id: int = 1


class ListagemchamadosSchema(BaseModel):
    """ Define como uma listagem de chamados será retornada.
    """
    chamados:List[ChamadoSchema]


def apresenta_chamados(chamados: List[Chamado]):
    """ Retorna uma representação do chamado seguindo o schema definido em
        ChamadoViewSchema.
    """
    result = []
    for chamado in chamados:
        result.append({
            "id": chamado.id,
            "nome": chamado.nome,
            "descricao": chamado.descricao,
            "prioridade": chamado.prioridade,
        })

    return {"chamados": result}


class ChamadoViewSchema(BaseModel):
    """ Define como um chamado será retornado: chamado
    """
    id: int = 1
    nome: str = "Gabriel"
    descricao: Optional[str] = "Descrever seu pedido"
    prioridade: str = "Medio"


class ChamadoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    id: int

def apresenta_chamado(chamado: Chamado):
    """ Retorna uma representação do chamado seguindo o schema definido em
        ChamadoViewSchema.
    """
    return {
        "id": chamado.id,
        "nome": chamado.nome,
        "descricao": chamado.descricao,
        "prioridade": chamado.prioridade,

    }

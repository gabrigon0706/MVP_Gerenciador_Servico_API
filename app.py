from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Chamado
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
chamado_tag = Tag(name="Chamados", description="Adição, visualização e remoção de Chamados à base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/chamado', tags=[chamado_tag],
          responses={"200": ChamadoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_chamado(form: ChamadoSchema):
    """Adiciona um novo Chamado à base de dados

    Retorna uma representação dos chamados
    """
    chamado = Chamado(
        nome=form.nome,
        descricao=form.descricao,
        prioridade=form.prioridade)
    logger.debug(f"Adicionando  nome do solicitante: '{chamado.nome}'")
    try:
        # criando conexão com a base
        session = Session()
        # criando chamado
        session.add(chamado)
        # efetivando a camanda de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado chamado: '{chamado.nome}'")
        return apresenta_chamado(chamado), 200

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar chamado '{chamado.nome}', {error_msg}")
        return {"mesage": error_msg}, 400


@app.get('/chamados', tags=[chamado_tag],
         responses={"200": ListagemchamadosSchema, "404": ErrorSchema})
def get_chamados():
    """Faz a busca por todos os Chamados cadastrados

    Retorna uma representação da listagem de chamados.
    """
    logger.debug(f"Coletando os chamados ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    chamados = session.query(Chamado).all()

    if not chamados:
        # se não há chamado 
        return {"chamados": []}, 200
    else:
        logger.debug(f"%d Chamados econtrados" % len(chamados))
        # retorna a representação do chamado
        print(chamados)
        return apresenta_chamados(chamados), 200


@app.delete('/chamado', tags=[chamado_tag],
            responses={"200": ChamadoDelSchema, "404": ErrorSchema})
def del_chamado(query: ChamadoBuscaSchema):
    """Deleta um Chamado a partir do id do ticket informado

    Retorna uma mensagem de confirmação da remoção.
    """
    chamado_id = ((query.id))
    print(chamado_id)
    logger.debug(f"Deletando dados sobre o chamado #{chamado_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Chamado).filter(Chamado.id == chamado_id).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado chamado #{chamado_id}")
        return {"mesage": "Chamado removido", "id": chamado_id}
    else:
        # se o chamado não foi encontrado
        error_msg = "Chamado não encontrado na base :/"
        logger.warning(f"Erro ao deletar chamado #'{chamado_id}', {error_msg}")
        return {"mesage": error_msg}, 404



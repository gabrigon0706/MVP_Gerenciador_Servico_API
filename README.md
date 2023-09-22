# API Prontuário Médico

Este é um projeto de MVP (Minimum Viable Product) de uma API Flask para gerenciar serviços.

Ela permite adicionar, visualizar e remover chamados da base de dados. Com o Gerenciado de serviço os analistas recebem a demanda e tem um aplicação rapida para a solução dessa solicitações.

## Requisitos

Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal.

Certifique-se de que você tenha  todas as libs python listadas no `requirements.txt` instaladas.

Este comando instala as bibliotecas, descritas no arquivo `requirements.txt`:

pip install -r requirements.txt

## Como Usar

Para utilizar esta API, siga os passos abaixo:

1. Inicie a aplicação Flask:

  flask run --host 0.0.0.0 --port 5000

2. Acesse a documentação Swagger para obter detalhes sobre as rotas e os parâmetros necessários.

3. Use as rotas para adicionar, visualizar ou atender.

## Documentação Swagger

Para obter a documentação completa desta API no estilo Swagger, acesse: 
[http://localhost:5000//openapi/swagger#/](http://localhost:5000//openapi/swagger#/)

## Rotas da API

- [POST] `/chamado`

  Adiciona um novo medicamento à base de dados.

  - **Entrada**: Um objeto JSON com os dados do chamado.
  - **Saída**: Uma representação do chamado cadastrado.


- [GET] `/chamados`

  Retorna uma listagem de todos os chamados cadastrados.

  
- [DELETE] `/chamado`

  Remove um chamado com base em seu Id.

## Notas de Versão

### Versão 1.0.0 (setembro/2023)

- Implementação inicial da API.
- Funcionalidade de adicionar, visualizar e atender.

## Autor

Este projeto foi desenvolvido por Gabriel Gonçalves e pode ser encontrado no [GitHub](https://github.com/gabrigon0706).

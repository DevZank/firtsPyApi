# API de Livros 📚

Projeto de estudo desenvolvido em Python com FastAPI para aprender, na prática, como funcionam rotas, requisições HTTP, parâmetros de caminho e respostas JSON.

## Funcionalidades

- Rota inicial com mensagem de boas-vindas.
- Listagem de títulos de livros.
- Consulta de um livro pelo ID.
- Mensagem para IDs não cadastrados.

Os dados estão definidos diretamente no código, sem banco de dados.

## Tecnologias

- Python
- FastAPI
- Uvicorn, servidor incluído na instalação padrão do FastAPI.

## Como executar

Os comandos abaixo são para Windows com PowerShell e devem ser executados na pasta do projeto. É necessário ter Python instalado.

**1. Crie o ambiente virtual:**

```powershell
python -m venv .venv
```

**2. Instale as dependências:**

```powershell
.\.venv\Scripts\python.exe -m pip install "fastapi[standard]"
```

**3. Inicie o servidor de desenvolvimento:**

```powershell
.\.venv\Scripts\fastapi.exe dev main.py
```

**4. Acesse no navegador:**

- API: http://127.0.0.1:8000
- Documentação interativa: http://127.0.0.1:8000/docs

Para encerrar o servidor, pressione `Ctrl+C` no terminal.

## Rotas

| Método | Caminho | Descrição |
|---|---|---|
| GET | `/` | Retorna a mensagem inicial |
| GET | `/livros` | Retorna uma string com três títulos |
| GET | `/livro/{livro_id}` | Consulta um dos livros cadastrados, com IDs de 1 a 10 |

### Exemplo de consulta

```http
GET /livro/6
```

Resposta:

```json
{
  "6": "Entendendo Algoritmos"
}
```

Para um ID não cadastrado:

```json
{
  "Erro": "Livro não encontrado"
}
```

Atualmente, a mensagem de livro não encontrado é devolvida com o status padrão `200`. O tratamento com status `404` será uma melhoria futura.

## Próximos passos

- Centralizar os livros em uma estrutura de dados.
- Retornar uma lista estruturada na rota `/livros`.
- Usar o status `404` para livros não encontrados.
- Adicionar cadastro, atualização e remoção de livros.
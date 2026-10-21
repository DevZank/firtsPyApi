# API de Livros 📚

Projeto de estudo desenvolvido em Python com FastAPI para aprender, na prática, como funcionam APIs, rotas HTTP, parâmetros de caminho, validação de dados e respostas JSON.

## Funcionalidades

- Listagem de todos os livros.
- Consulta de um livro pelo ID.
- Cadastro de novos livros.
- Atualização completa de livros.
- Remoção de livros.
- Validação dos dados recebidos.
- Retorno de erro `404` quando o livro não existe.

Os dados são armazenados em um dicionário na memória, sem banco de dados. Por isso, alterações são perdidas quando o servidor é reiniciado.

## Tecnologias

- Python
- FastAPI
- Pydantic
- Uvicorn

## Como executar

Os comandos abaixo devem ser executados na pasta do projeto usando o PowerShell. É necessário ter Python instalado.

### 1. Criar o ambiente virtual

```powershell
python -m venv .venv
```

### 2. Instalar as dependências

```powershell
.\.venv\Scripts\python.exe -m pip install "fastapi[standard]"
```

### 3. Iniciar o servidor

```powershell
.\.venv\Scripts\fastapi.exe dev main.py
```

### 4. Acessar a API

- API: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Documentação interativa: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Para encerrar o servidor, pressione `Ctrl+C` no terminal.

## Formato de um livro

```json
{
  "nome": "O Hobbit",
  "preco": 46.90,
  "sinopse": "Bilbo embarca em uma aventura épica.",
  "imagem": "https://exemplo.com/o-hobbit.jpg"
}
```

## Rotas

| Método | Caminho | Descrição |
|---|---|---|
| GET | `/` | Retorna uma mensagem inicial |
| GET | `/livros` | Lista todos os livros |
| GET | `/livros/{livro_id}` | Consulta um livro pelo ID |
| POST | `/livros` | Cadastra um novo livro |
| PUT | `/livros/{livro_id}` | Substitui os dados de um livro |
| DELETE | `/livros/{livro_id}` | Remove um livro |

## Exemplos

### Consultar um livro

```http
GET /livros/1
```

### Cadastrar um livro

```http
POST /livros
```

Corpo da requisição:

```json
{
  "nome": "O Programador Pragmático",
  "preco": 70.50,
  "sinopse": "Conceitos importantes para desenvolver software melhor.",
  "imagem": "https://exemplo.com/programador.jpg"
}
```

### Atualizar um livro

```http
PUT /livros/1
```

O corpo deve conter todos os campos do livro.

### Remover um livro

```http
DELETE /livros/1
```

Não é necessário enviar corpo nessa requisição.

## Tratamento de erros

Quando um ID não existe, a API retorna o status `404`:

```json
{
  "detail": "Livro não encontrado!"
}
```

## Próximos passos

- Salvar os dados em um arquivo JSON.
- Permitir alterações persistentes após reiniciar o servidor.
- Criar rotas para leitores.
- Criar sistema de empréstimos e devoluções.
- Adicionar testes automatizados.
- Melhorar o controle de estoque e disponibilidade dos livros.
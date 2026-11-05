from typing import Optional

from markdown_it.rules_block import table
from sqlmodel import Field, SQLModel

class Livro(SQLModel, table=True):
    __tablename__ = "livros"

    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    preco: float
    sinopse: str
    imagem: str
    estoque: int = 0

class Usuario(SQLModel, table=True):
    __tablename__ = "usuarios"

    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    email: str
    telefone: int
    senha: str
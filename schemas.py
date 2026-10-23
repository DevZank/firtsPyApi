from pydantic import BaseModel, Field

class LivroCriacao(BaseModel):
    nome: str = Field(min_length=1)
    preco: float = Field(ge=0)
    sinopse: str
    imagem: str
    estoque: int = Field(default=0, ge=0)

class LivroAtualizacao(BaseModel):
    nome: str = Field(min_length=1)
    preco: float = Field(ge=0)
    sinopse: str
    imagem: str
    estoque: int = Field(ge=0)
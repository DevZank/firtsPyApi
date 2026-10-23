from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, select
from database import criar_tabelas, obter_sessao
from schemas import LivroAtualizacao, LivroCriacao
from models import Livro

app = FastAPI()

criar_tabelas()

@app.get("/")
def inicio():
    return {"mensagem": "Successfully connected!"}

@app.get("/livros")
def listar_livros(
    sessao: Session = Depends(obter_sessao)
):
    comando = select(Livro)
    livros = sessao.exec(comando).all()

    return livros

@app.get("/livros/{livro_id}")
def buscar_livro(livro_id: int, sessao: Session = Depends(obter_sessao)):
    livro = sessao.get(Livro, livro_id)

    if livro is None:
        raise HTTPException(
            status_code=404,
            detail='Livro não encontrado!'
        )
    return livro

@app.post("/livros")
def postar_livro(
    dados_livro: LivroCriacao, sessao: Session = Depends(obter_sessao)
):

    novo_livro = Livro(
        nome=dados_livro.nome,
        preco=dados_livro.preco,
        sinopse=dados_livro.sinopse,
        imagem=dados_livro.imagem,
        estoque=dados_livro.estoque
    )

    sessao.add(novo_livro)
    sessao.commit()
    sessao.refresh(novo_livro)

    return novo_livro

@app.put("/livros/{livro_id}")
def atualizar_livro(
        livro_id: int,
        dados_livro: LivroAtualizacao,
        sessao: Session = Depends(obter_sessao)
):
    livro = sessao.get(Livro, livro_id)

    if livro is None:
        raise HTTPException(
            status_code=404,
            detail="Livro não encontrado!"
        )

    livro.nome = dados_livro.nome
    livro.preco = dados_livro.preco
    livro.sinopse = dados_livro.sinopse
    livro.imagem = dados_livro.imagem
    livro.estoque = dados_livro.estoque

    sessao.commit()
    sessao.refresh(livro)

    return livro

@app.delete("/livros/{livro_id}")
def deletar_livros(livro_id: int, sessao: Session = Depends(obter_sessao)):
    livro = sessao.get(Livro, livro_id)

    if livro is None:
        raise HTTPException(
            status_code=404,
            detail='Livro não encontrado!'
        )

    sessao.delete(livro)
    sessao.commit()

    return {
        "mensagem": "Livro removido com sucesso!",
        "id": livro_id
    }
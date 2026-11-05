from schemas import (
    LivroAtualizacao,
    LivroCriacao,
    UsuarioCriacao, 
    UsuarioLogin
)

from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, select
from database import criar_tabelas, obter_sessao
from models import Livro, Usuario
from security import gerar_hash_senha, criar_token, verificar_senha

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

@app.get("/usuarios")
def listar_usuarios(
    sessao: Session = Depends(obter_sessao)
):
    comando = select(Usuario)
    usuarios = sessao.exec(comando).all()

    return usuarios

@app.get("/usuarios/{usuario_id}")
def buscar_usuario(usuario_id: int, sessao: Session = Depends(obter_sessao)):
    usuario = sessao.get(Usuario, usuario_id)

    if usuario is None:
        raise HTTPException(
            status_code=404,
            detail='Usuário não encontrado!'
        )
    return usuario

@app.post("/usuarios")
def criar_usuario(
    dados_usuario: UsuarioCriacao, sessao: Session = Depends(obter_sessao)    
):

    novo_usuario = Usuario(
        nome=dados_usuario.nome,
        email=dados_usuario.email,
        telefone=dados_usuario.telefone,
        senha=gerar_hash_senha(dados_usuario.senha)
    )

    sessao.add(novo_usuario)
    sessao.commit() 
    sessao.refresh(novo_usuario)

    return {
        "id": novo_usuario.id,
        "nome": novo_usuario.nome,
        "email": novo_usuario.email,
        "telefone": novo_usuario.telefone, 
    }

@app.put("/usuarios/{usuario_id}")
def atualizar_usuario(
        usuario_id: int,
        dados_usuario: UsuarioCriacao,
        sessao: Session = Depends(obter_sessao)
):
    usuario = sessao.get(Usuario, usuario_id)

    if usuario is None:
        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado!"
        )

    usuario.nome = dados_usuario.nome
    usuario.email = dados_usuario.email
    usuario.telefone = dados_usuario.telefone
    usuario.senha = dados_usuario.senha

    sessao.commit()
    sessao.refresh(usuario)

    return usuario  

@app.delete("/usuarios/{usuario_id}")
def deletar_usuario(usuario_id: int, sessao: Session = Depends(obter_sessao)):
    usuario = sessao.get(Usuario, usuario_id)

    if usuario is None:
        raise HTTPException(
            status_code=404,
            detail='Usuário não encontrado!'
        )

    sessao.delete(usuario)
    sessao.commit()

    return {
        "mensagem": "Usuário removido com sucesso!",
        "id": usuario_id
    }

@app.post("/login")
def login(
    dados_login: UsuarioLogin,
    sessao: Session = Depends(obter_sessao)
):
    comando = select(Usuario).where(
        Usuario.email == dados_login.email
    )

    usuario = sessao.exec(comando).first()

    if usuario is None or not verificar_senha(
        dados_login.senha,
        usuario.senha
    ):
        raise HTTPException(
            status_code=401,
            detail="Email ou senha inválidos"
        )

    token = criar_token(usuario.email)

    return {
        "access_token": token,
        "token_type": "bearer"
    }
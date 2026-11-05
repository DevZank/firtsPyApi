from datetime import datetime, timedelta, timezone
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from pwdlib import PasswordHash
from sqlmodel import Session, select

from database import obter_sessao
from models import Usuario

password_hash = PasswordHash.recommended()

CHAVE_SECRETA = "TOKEN_SUPER_SECRETO"
ALGORITMO = "HS256"
TEMPO_TOKEN_MINUTOS = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def gerar_hash_senha(senha: str) -> str:
    return password_hash.hash(senha)


def verificar_senha(senha: str, senha_hash: str) -> bool:
    return password_hash.verify(senha, senha_hash)


def criar_token(email: str) -> str:
    expiracao = datetime.now(timezone.utc) + timedelta(
        minutes=TEMPO_TOKEN_MINUTOS
    )

    dados = {
        "sub": email,
        "exp": expiracao
    }

    return jwt.encode(
        dados,
        CHAVE_SECRETA,
        algorithm=ALGORITMO
    )


def obter_usuario_atual(
    token: str = Depends(oauth2_scheme),
    sessao: Session = Depends(obter_sessao)
):
    credenciais_invalidas = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token inválido ou expirado",
        headers={"WWW-Authenticate": "Bearer"}
    )

    try:
        dados = jwt.decode(
            token,
            CHAVE_SECRETA,
            algorithms=[ALGORITMO]
        )

        email = dados.get("sub")

        if email is None:
            raise credenciais_invalidas

    except JWTError:
        raise credenciais_invalidas

    usuario = sessao.exec(
        select(Usuario).where(Usuario.email == email)
    ).first()

    if usuario is None:
        raise credenciais_invalidas

    return usuario
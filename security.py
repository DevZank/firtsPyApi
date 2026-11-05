from datetime import datetime, timedelta, timezone
from jose import jwt
from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()

CHAVE_SECRETA = "TOKEN_SUPER_SECRETO"
ALGORITMO = "HS256"
TEMPO_TOKEN_MINUTOS = 30

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

    return jwt.encode(dados, CHAVE_SECRETA, algorithm=ALGORITMO)
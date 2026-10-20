from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensagem": "Hello, World!"}

@app.get("/livros")
def livros():
    return {"livros": "Harry Potter, Os segredos da mente milionária, O Hobbit"}

@app.get("/livro/{livro_id}")
def livro(livro_id: int):
    if livro_id == 1:
        return {"1": "Harry Potter"}
    elif livro_id == 2:
        return {"2": "O Hobbit"}
    elif livro_id == 3:
        return {"3": "Os segredos da mente milionária"}
    elif livro_id == 4:
        return {"4": "A última onda"}
    elif livro_id == 5:
        return {"5": "Como fazer amigos e influenciar pessoas"}
    elif livro_id == 6:
        return {"6": "Entendendo Algoritmos"}
    elif livro_id == 7:
        return {"7": "Pai Rico Pai Pobre"}
    elif livro_id == 8:
        return {"8": "A Coragem de ser imperfeito"}
    elif livro_id == 9:
        return {"9": "A Coragem de ser imperfeito"}
    elif livro_id == 10:
        return {"10": "Dicionário Escolar Língua Portuguesa"}
    else:
        return {"Erro": "Livro não encontrado"}
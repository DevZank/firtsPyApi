from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensagem": "Hello, World!"}

@app.get("/livros")
def livros():
    return {"livros": "Harry Potter, Os segredos da mente milionária, O Hobbit"}
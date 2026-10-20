from fastapi import FastAPI, HTTPException

app = FastAPI()

livros = {
    1: {
        "nome": "O Hobbit",
        "preco": 46.90,
        "sinopse": "Bilbo embarca numa aventura épica para recuperar um tesouro guardado por um dragão.",
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_896060-MLA112164692152_062026-F.webp"
    },
    2: {
        "nome": "Harry Potter",
        "preco": 36.48,
        "sinopse": "Harry descobre ser bruxo e enfrenta mistérios em seu primeiro ano em Hogwarts.",
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_847575-MLA113308006353_062026-F.webp"
    },
    3: {
        "nome": "A Próxima Onda",
        "preco": 48.67,
        "sinopse": "IA e biotecnologia prometem revolucionar o mundo e desafiar nosso controle.",
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_767336-MLA110511197720_052026-F.webp"
    },
    4: {
        "nome": "Os segredos da mente milionária",
        "preco": 33.29,
        "sinopse": "Descubra como mudar sua mentalidade financeira e construir riqueza.",
        "imagem": "https://http2.mlstatic.com/D_Q_NP_958059-MLB51616879105_092022-F-livro-fisico-os-segredos-da-mente-milionaria-de-t-harv-eker.webp"
    },
    5: {
        "nome": "Como fazer amigos e influenciar pessoas",
        "preco": 22.19,
        "sinopse": "Aprenda a conquistar pessoas, criar conexões e melhorar seus relacionamentos.",
        "imagem": "https://http2.mlstatic.com/D_Q_NP_961753-MLA105125815116_012026-F.webp"
    },
    6: {
        "nome": "Entendendo Algoritmos",
        "preco": 72.67,
        "sinopse": "Aprenda algoritmos de forma simples, visual e prática para resolver problemas.",
        "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_947824-MLA115989316122_092026-F-livro-entendendo-algoritmos-2a-edicao.webp"
    },
    7: {
        "nome": "Pai Rico Pai Pobre",
        "preco": 44.18,
        "sinopse": "Aprenda a pensar sobre dinheiro, investir e construir sua independência financeira.",
        "imagem": "https://http2.mlstatic.com/D_Q_NP_631924-MLU74994562986_032024-F.webp"
    },
    8: {
        "nome": "A Coragem de ser imperfeito",
        "preco": 33.29,
        "sinopse": "Aprenda a abraçar suas imperfeições e viver com coragem e autenticidade.",
        "imagem": "https://http2.mlstatic.com/D_Q_NP_704968-MLB51616486641_092022-F-livro-fisico-a-coragem-de-ser-imperfeito-brene-brown.webp"
    },
    9: {
        "nome": "Dicionário Escolar Língua Portuguesa",
        "preco": 56.72,
        "sinopse": "Amplie seu vocabulário e aprenda significados e usos das palavras em português.",
        "imagem": "https://http2.mlstatic.com/D_Q_NP_964168-MLB112999180962_072026-F-dicionario-escolar-michaelis-ensino-fundamental.webp"
    }
}

@app.get("/")
def inicio():
    return {"mensagem": "Successfully connected!"}

@app.get("/livros")
def listar_livros():
    return livros

@app.get("/livros/{livro_id}")
def buscar_livro(livro_id: int):
    if livro_id not in livros:
        raise HTTPException(
            status_code=404,
            detail="Livro não encontrado!"
        )
    return livros[livro_id]


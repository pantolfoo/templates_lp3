from flask import Flask, render_template, request
from validate_docbr import CPF, CNPJ

# nome da aplicação 
app = Flask (__name__)

# rotas sem direcionamento:
@app.route("/cpf")
def gerar_cpf():
    cpf = CPF ()
    cpf_retorno = cpf.generate((True))
    return render_template("cpf.html", cpf = cpf_retorno)

@app.route("/cnpj")
def gerar_cnpj():
    cnpj = CNPJ ()
    cnpj_retorno = cnpj.generate((True))
    return render_template("cnpj.html", cnpj = cnpj_retorno)


# rotas com direcionamento:
@app.route ("/")
def home():
    return render_template ('home.html')

@app.route ("/contato")
def contato():
    return render_template ('contato.html')
    
@app.route ("/termosdeuso")
def termosdeuso():
    return render_template ('termosdeuso.html')

@app.route ("/politicadeprivacidade")
def politicadeprivacidade():
    return render_template ('politicadeprivacidade.html')

@app.route ("/comoutilizar")
def comoutilizar():
    return render_template ('comoutilizar.html')


# lista de produtos:
lista_produtos = [
    {"nome": "É assim que começa", "genero": "Romance", "autor": "Coolen Hoover"},
    {"nome": "É assim que acaba", "genero": "Romance", "autor": "Coolen Hoover"},
    {"nome": "Todas as suas (im)perfeições", "genero": "Romance", "autor": "Coolen Hoover"},
]


@app.route("/produtos")
def produtos():
    lista_produtos = [
        {"nome": "É assim que acaba", "genero": "Romance", "autor": "Colleen Hoover", "img": "1"},
        {"nome": "É assim que começa", "genero": "Romance", "autor": "Colleen Hoover", "img": "2"},
        {"nome": "Todas as suas (im)perfeições", "genero": "Romance", "autor": "Colleen Hoover", "img": "3"},
    ]

    return render_template("produtos.html", produtos=lista_produtos) 

@app.route("/produtos/cadastro")
def cadastro_produto():
    return render_template("cadastroproduto.html")

@app.route("/produtos/cadastro", methods=['POST'])
def salvar_produtos():
    nome = request.form  ['nome']#dicionario imnutavel
    genero = request.form  ['genero']
    autor = request.form ['autor']

    produto = { "nome": nome, "genero": genero, "autor": autor}

    lista_produtos.append(produto)
    return render_template("produtos.html", produtos = lista_produtos) 

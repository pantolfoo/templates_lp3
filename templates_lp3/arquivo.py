def obter_produtos():
    with open ("produtos.csv", "r") as arquivo_produtos:
        produtos = []
        for linha in arquivo_produtos:
            dados_produtos = linha.strip().split(",")
            produto = {
                "nome": dados_produtos[0],
                "descricao": dados_produtos[1],
                "preco": float (dados_produtos[2]),
                "imagem": dados_produtos[3]  
            }
            produtos.append(produto)
    return produtos
print (obter_produtos())

def salvar_produto (nome, descricao, preco, imagem):
    with open ("produtos.csv", "a") as arquivo_produtos:
        texto_produto = f"\n{nome},{descricao},{preco},{imagem}"
        arquivo_produtos.write(texto_produto)
salvar_produto("Celular", "Tira foto", 3.500, "celular.jpg")
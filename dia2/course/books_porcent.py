import json
import csv

def recupera_json_livros(arquivo):
    return json.load(arquivo)

def conta_livros_por_categoria(livros):
    categorias={}
    for livro in livros:
        for categoria in livro["categories"]:
            if not categorias.get(categoria):
                categorias[categoria] = 0
            categorias[categoria] += 1
    return categorias

def calcula_porcentagem_por_categoria(livro_por_categoria,total_de_livros):
    return [
        [categoria, num_livros / total_de_livros]
        for categoria, num_livros in livro_por_categoria.items()
    ]

def cria_arquivo_csv(arquivo,cabecalho,linhas):
    writer = csv.writer(arquivo)
    writer.writerow(cabecalho)
    writer.writerows(linhas)

if __name__ == "__main__":
    with open('books.json') as arquivo:
        livros = recupera_json_livros(arquivo)
        livro_por_categoria = conta_livros_por_categoria(livros)
        total_de_livros = len(livros)
        linhas_porcentagem= calcula_porcentagem_por_categoria(livro_por_categoria,total_de_livros)
    cabecalho = ['categoria','porcentagem']
    with open('report.csv', 'w') as arquivo:
            cria_arquivo_csv(arquivo,cabecalho,linhas_porcentagem)
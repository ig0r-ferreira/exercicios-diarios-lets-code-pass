"""
🧠 EXERCÍCIO DO DIA 💭

1️⃣ 🅰️ Crie um programa que leia uma matriz 10 x 10 e escreva a localização (linha e a coluna)
do maior valor.

"""


def encontrar_maior_valor(matriz_):
    maiores_por_linha = list(map(max, matriz_))
    maior = max(maiores_por_linha)

    index_linha = maiores_por_linha.index(maior)

    return {
        'valor': maior,
        'linha': index_linha,
        'coluna': matriz_[index_linha].index(maior)
    }


def gerar_matriz(qtd_linhas, qtd_colunas):
    from random import sample

    tamanho_matriz = qtd_linhas * qtd_colunas
    numeros_aleatorios = sample(range(tamanho_matriz * 2 + 1), k=tamanho_matriz)

    matriz_ = [numeros_aleatorios[i: i + qtd_colunas] for i in range(0, tamanho_matriz, qtd_linhas)]

    return matriz_


matriz = gerar_matriz(10, 10)
dados_maior = encontrar_maior_valor(matriz)

print(f'Matriz 10 x 10:\n\n' + '\n'.join(map(lambda linha: '\t'.join(map(str, linha)), matriz)) + '\n\n'
      f'Maior valor: {dados_maior.get("valor")}\n'
      f'Linha: {dados_maior.get("linha") + 1}\nColuna: {dados_maior.get("coluna") + 1}')

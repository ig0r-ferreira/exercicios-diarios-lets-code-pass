"""

1️⃣ 🅱️ Crie um programa que leia uma matriz 6 x 6, conte e escreva quantos valores maiores que 10
ela possui.

"""


def gerar_matriz(qtd_linhas, qtd_colunas):
    from random import sample

    tamanho_matriz = qtd_linhas * qtd_colunas
    numeros_aleatorios = sample(range(tamanho_matriz * 2 + 1), k=tamanho_matriz)

    matriz_ = [numeros_aleatorios[i: i + qtd_colunas] for i in range(0, tamanho_matriz, qtd_linhas)]

    return matriz_


matriz = gerar_matriz(6, 6)
maiores_que_dez = [elemento for linha in matriz for elemento in linha if elemento > 10]

print(f'Matriz 6 x 6:\n' + '\n'.join(map(lambda linha: '\t'.join(map(str, linha)), matriz)) + '\n\n'
      f'A matriz contém {len(maiores_que_dez)} elementos maiores que DEZ!\n'
      f'São eles: {sorted(maiores_que_dez)}')

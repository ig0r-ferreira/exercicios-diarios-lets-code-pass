"""
🧠 EXERCÍCIO DO DIA 💭 - DESAFIO

5️⃣ No jogo Sudoku temos uma matriz 9 × 9 dividida em 9 quadrados de 3 × 3 preenchidos previamente
com alguns números entre 1 e 9 (veja o exemplo à esquerda abaixo). Uma solução para uma instância
do jogo consiste no preenchimento de todas as posições vazias com números entre 1 e 9 respeitando-se
as seguintes regras:

(a) Não pode haver números repetidos em um mesmo quadrado, ou seja, cada número entre 1 e 9 deve
aparecer exatamente uma vez em cada quadrado.
(b) Não pode haver números repetidos em nenhuma linha da matriz.
(c) Não pode haver números repetidos em nenhuma coluna da matriz.

Escreva uma função que receba uma matriz 9 × 9 como parâmetro, que represente uma proposta de solução
para um Sudoku, e teste se a matriz é uma solução válida para o jogo, devolvendo True em caso
verdadeiro e False, caso contrário. A seguinte função deve ser implementada:

1 def solucao ( mat ) :
"""


def existe_duplicado(lista):
    return any([num for num in lista if lista.count(num) > 1])


def solucao(matriz):
    assert len(matriz) == 9, 'Erro: Matriz de tamanho inválido! A matriz deve ser 9 x 9.'

    for i, linha_ in enumerate(matriz):
        assert len(linha_) == 9, 'Erro: Matriz de tamanho inválido! A matriz deve ser 9 x 9.'
        assert max(linha_) < 10 and min(linha_) > 0, 'Erro: Elementos fora do intervalo de 1 a 9!'

        if existe_duplicado(linha_) or existe_duplicado([matriz[j][i] for j in range(len(linha_))]):
            return False

    return True


sudoku_resolvido = [
    [4, 2, 6, 5, 7, 1, 3, 9, 8],
    [8, 5, 7, 2, 9, 3, 1, 4, 6],
    [1, 3, 9, 4, 6, 8, 2, 7, 5],
    [9, 7, 1, 3, 8, 5, 6, 2, 4],
    [5, 4, 3, 7, 2, 6, 8, 1, 9],
    [6, 8, 2, 1, 4, 9, 7, 5, 3],
    [7, 9, 4, 6, 3, 2, 5, 8, 1],
    [2, 6, 5, 8, 1, 4, 9, 3, 7],
    [3, 1, 8, 9, 5, 7, 4, 6, 2]
]

print('\n' + '-' * 31)
for index_linha, linha in enumerate(sudoku_resolvido):
    print('|', end='')
    for index_coluna, coluna in enumerate(linha):
        print(f' {coluna} ', end='|' if (index_coluna + 1) % 3 == 0 else '')
    else:
        print('\n' + '-' * 31 if (index_linha + 1) % 3 == 0 else '')

try:
    print(f'\nSolução proposta para o SUDOKU é válida? {"SIM" if solucao(sudoku_resolvido) else "NÃO"}')
except Exception as erro:
    print(f'\033[1;31m{erro}\033[m')

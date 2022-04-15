"""

2️⃣ 🅱 Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘ | ‘.
Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o
valor mínimo igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, eles
devem ser modificados para valores dentro da faixa de forma elegante.
"""


def formatar_dimensao(valor):
    return valor if 20 >= valor >= 1 else 1 if valor < 1 else 20


def montar_retangulo(linhas=1, colunas=20):
    linhas = formatar_dimensao(linhas)
    colunas = formatar_dimensao(colunas)

    aresta_vertical = '+' + ('-' * colunas) + '+'
    aresta_horizontal = '|' + (' ' * colunas) + '|'

    print(f'{aresta_vertical}\n' + '\n'.join([aresta_horizontal] * linhas) + f'\n{aresta_vertical}')


montar_retangulo()

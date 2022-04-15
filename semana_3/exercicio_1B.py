"""
1️⃣ 🅱️ Faça um programa para imprimir:

1
1   2
1   2   3
.....
1   2   3   ...  n


para um n informado pelo usuário. Use uma função que receba um valor n inteiro e
imprima até a n-ésima linha.

"""

while True:
    try:
        n = int(input('Informe um valor inteiro positivo: ').strip())
    except ValueError:
        print('\033[1;31mErro: Você não informou um número!\033[m')
    else:
        if n > 0:
            break
        print('\033[1;31mErro: Informe um inteiro positivo!\033[m')

for i in range(1, n + 1):
    print(' '.join(map(str, range(1, i + 1))))

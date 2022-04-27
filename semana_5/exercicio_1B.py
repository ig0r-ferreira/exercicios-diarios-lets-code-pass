"""

🧠 EXERCÍCIO DO DIA 💭

Faça um programa que leia um ano (valor inteiro) e imprima se ele é bissexto ou não.
Observação: um ano é bissexto se ele é múltiplo de 400, ou se ele é múltiplo de 4 mas não é múltiplo
de 100.

"""


def bissexto(ano):
    return ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0


while True:
    try:
        ano_ = int(input('Digite um ano para verificar se ele é bissexto: ').strip())
    except ValueError:
        print('\033[1;31mErro: Você não informou um número. Tente novamente!\033[m')
    else:
        if ano_ > 0:
            break

        print('\033[1;31mErro: O valor deve ser maior que zero!\033[m')


print(f'\n{ano_} {"" if bissexto(ano_) else "NÃO "}é um ano bissexto.')

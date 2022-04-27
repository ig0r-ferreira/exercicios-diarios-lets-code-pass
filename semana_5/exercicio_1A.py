"""
🧠 EXERCÍCIO DO DIA 💭

1️⃣ 🅰️ Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre o mais barato.

"""


def perguntar_preco(msg):
    while True:
        try:
            preco = float(input(msg))
        except ValueError:
            print('\033[1;31mErro: Você não informou um valor. Tente novamente!\033[m')
        else:
            if preco > 0:
                return preco

            print('\033[1;31mErro: O valor deve ser maior que zero!\033[m')


precos = [perguntar_preco(f'Informe o preço do {i}º produto: R$ ') for i in range(1, 4)]
print(f'Dos {len(precos)} produtos informados, o mais barato custa R$ {min(precos):.2f}.')

"""
🧠 EXERCÍCIO DO DIA 💭

2️⃣ Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número e:

Par ou ímpar;
Positivo ou negativo;

"""


import decimal
import re

decimal.getcontext().prec = 9

while True:
    try:
        entradas = input().strip().split(' ')

        if entradas[-1] not in ['+', '-', '/', '*'] or \
                any([re.match(r'^-?(\d+|\d+\.\d+)$', e) is None for e in entradas[:-1]]):
            raise ValueError

        expressao = entradas[-1].join(list(map(lambda e: f'decimal.Decimal(\'{e}\')', entradas[:-1])))
        result = decimal.Decimal(eval(expressao))

        print(f'RESULTADO: {result}\t\t{"" if not result == int(result) else " PAR" if result % 2 == 0 else " ÍMPAR"} '
              f'{"POSITIVO" if result > 0 else "NEGATIVO" if result != 0 else "NEUTRO"}')

    except ValueError:
        print('\033[1;31mErro: Operação inválida. Tente novamente!\033[m')
    except ZeroDivisionError:
        print('\033[1;31mErro: Não é possível efetuar divisão por zero!\033[m')
    except EOFError:
        break

"""
🧠 EXERCÍCIO DO DIA 💭

2️⃣ Considere um programa que deve classificar um número como par ou ímpar e, além disso,
classificar ele como menor do que 100 ou maior ou igual a 100.
Escreva um programa que faça essa classificação corretamente.

"""

while True:
    try:
        num = int(input('Digite um número: ').strip())
    except ValueError:
        print('Erro: Você não digitou um número!')
    else:
        break

print(f'{num} é {"PAR" if num % 2 == 0 else "ÍMPAR"} e'
      f' é {"MAIOR" if num > 100 else "IGUAL" if num == 100 else "MENOR"} a 100.')

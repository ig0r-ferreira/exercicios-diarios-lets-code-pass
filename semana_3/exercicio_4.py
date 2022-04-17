"""
🧠 EXERCÍCIO DO DIA 💭

4️⃣ Escreva uma função que receba dois números inteiros positivos a e b como parâmetro e determine
se eles são amigos ou não, devolvendo True caso sejam amigos e False caso contrário. Dois números
são amigos se cada número é igual à soma dos divisores próprios do outro (os divisores próprios de
um número m são os divisores estritamente menores que m).

Por exemplo, os divisores próprios de 220 são 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 e 110,
cuja soma é 284; e os divisores próprios de 284 são 1, 2, 4, 71 e 142, cuja soma é 220.
Logo, 220 e 284 são números amigos. A seguinte função deve ser implementada:

1 def amigos (a , b ) :

"""


def somar_divisores(n):
    return sum([num for num in range(1, n) if n % num == 0])


def amigos(a, b):
    return somar_divisores(a) == b and somar_divisores(b) == a


def solicitar_numero(texto):
    while True:
        try:
            num = int(input(f'{texto} ').strip())
        except ValueError:
            print('\033[1;31mErro: Você não informou um número!\033[m')
        else:
            return num


num1 = solicitar_numero('Digite um número:')
num2 = solicitar_numero('Digite outro número:')

print(f'\n{num1} e {num2} {"são" if amigos(num1, num2) else "não são"} amigos!')

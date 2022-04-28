"""
🧠 EXERCÍCIO DO DIA 💭

3️⃣ Faça um programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores, de fato,
podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou
escaleno.
Dicas: Três lados formam um triângulo quando a soma de quaisquer dos dois lados é maior que o terceiro.

Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;

"""


def solicitar_valor(msg):
    while True:
        try:
            valor = float(input(msg).strip())
        except ValueError:
            print('\033[1;31mErro: Você não informou um valor!\033[m')
        else:
            if valor > 0:
                return valor
            print('\033[1;31mErro: O valor deve ser maior que ZERO!\033[m')


while True:
    try:
        retas = sorted([solicitar_valor(f'Comprimento da {i}ª reta: ') for i in range(1, 4)])
        print()
        if not sum(retas[:-1]) > retas[-1]:
            print('Os comprimentos das retas não formam um triângulo!', end='\n' * 2)
        else:
            tipos_triangulos = {1: 'EQUILÁTERO', 2: 'ISÓSCELES', 3: 'ESCALENO'}
            print(f'Os comprimentos das retas formam um triângulo {tipos_triangulos[len(set(retas))]}.', end='\n' * 2)
    except (EOFError, KeyboardInterrupt):
        break

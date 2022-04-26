"""
🧠 EXERCÍCIO DO DIA 💭

3️⃣ Escreva um programa que leia uma sequência de números inteiros e os salve em uma lista.
Em seguida o programa deve ler um outro número inteiro C. O programa deve então encontrar dois números
de posições distintas da lista cuja multiplicação seja C e imprimí-los. Caso não existam tais números,
o programa deve imprimir uma mensagem correspondente. Exemplo:

Lista = [1, 2, 4, 5, 8, 10]
C = 8
Resultado: 1 e 8, 2 e 4

Lista = [2, 4, 5, 10, 7]
C = 35
Resultado: 5 e 7

Lista = [2, 4, 5, 10, 7]
C = 25
Resultado: não existem tais números

"""


while True:
    try:
        numeros = list(map(int, input('\nSequência de números inteiros: ').strip().split(' ')))
        C = int(input('Digite um número: '))

        ocorrencias = []
        for pos, num in enumerate(sorted(numeros)):

            num2 = C // num

            if C % num == 0 and num2 in numeros and numeros.index(num2) != pos and [num2, num] not in ocorrencias:
                ocorrencias.append(sorted([num, num2]))

        print(f'Não há na sequência dois números cujo o produto seja {C}!' if len(ocorrencias) == 0 else
              f'{ocorrencias} são os números da sequência cujo o produto é {C}!')

    except EOFError:
        break

"""
🧠 EXERCÍCIO DO DIA 💭

3️⃣ Escreva um programa que leia uma sequência de números inteiros e os salve em uma lista.
Em seguida o programa deve ler um outro número inteiro C. O programa deve então encontrar dois números
de posições distintas da lista cuja multiplicação seja C e imprimí-los. Caso não existam tais números,
o programa deve imprimir uma mensagem correspondente. Exemplo:

Lista = [2, 4, 5, 10, 7]
C = 35
Resultado: 5 e 7

Lista = [2, 4, 5, 10, 7]
C = 25
Resultado: não existem tais números

"""

while True:
    try:
        numeros = list(map(int, input('Sequência de números inteiros: ').strip().split(' ')))
        C = int(input('Digite um número: '))

        for pos, num in enumerate(sorted(numeros)):

            if C % num == 0 and C / num in numeros and numeros.index(C / num) != pos:
                print(f'{num} e {numeros[numeros.index(C / num)]} são os números da sequência cujo o produto é {C}!')
                break
        else:
            print(f'Não há na sequência dois números cujo o produto seja {C}!')
    except EOFError:
        break

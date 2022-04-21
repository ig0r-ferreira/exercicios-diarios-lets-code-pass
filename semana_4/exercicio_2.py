"""
🧠 EXERCÍCIO DO DIA 💭

2️⃣ Escreva um programa que leia duas sequências de n e m valores inteiros, onde n ≤ m, e
imprima quantas vezes a primeira sequência ocorre na segunda. Exemplo:

Primeira sequência: 1 0 1
Segunda sequência: 1 1 0 1 0 1 0 0 1 1 0 1 0
Resultado: 3

"""


def contar_subexp(subexp, exp):
    exp = ''.join(map(str, exp)) if type(exp) == list else str(exp)
    subexp = ''.join(map(str, subexp)) if type(subexp) == list else str(subexp)

    inicio = exp.find(subexp)

    if inicio == -1:
        return 0

    return 1 + contar_subexp(subexp, exp[inicio + 1:])


print(contar_subexp([1, 0, 1], [1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0]))
print(contar_subexp('GeeksforGeeks', 'GeeksforGeeksforGeeksforGeeks'))

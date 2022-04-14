"""
🧠 EXERCÍCIO DO DIA 💭

1️⃣ Faça um programa que leia um número n. Após isso, o seu programa deve ler uma sequência de
n números e imprimir uma mensagem indicando se a sequência lida está ordenada de forma crescente ou não.

"""


def solicitar_numero(texto):
    while True:
        try:
            num = int(input(texto).strip())
        except ValueError:
            print('Erro: Você não informou um número!')
        else:
            return num


def identificar_ordem(lista):
    lista_cresc = sorted(lista)

    return "CRESCENTE" if lista == lista_cresc else "DECRESCENTE" if lista == lista_cresc[::-1] else "ALEATÓRIA"


while True:
    n = solicitar_numero('Digite quantos números serão: ')

    if n >= 2:
        break

    print('2 é o valor mínimo!')


numeros = []
for i in range(n):
    numeros.append(solicitar_numero('Digite um número: '))


print(f'\nLista: {numeros}\nOrdem: {identificar_ordem(numeros)}')

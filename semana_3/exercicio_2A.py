"""
🧠 EXERCÍCIO DO DIA 💭

2️⃣ 🅰 Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais:
 taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem, e custo, que é o custo
 de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

"""


def somar_imposto(valor_original, taxa_imposto=0.0):
    return valor_original * (1 + (taxa_imposto / 100))


def solicitar_valor(texto):
    while True:
        try:
            valor = float(input(texto).strip())
        except ValueError:
            print('Erro: Informe um valor!')
        else:
            if valor > 0:
                return valor
            print('Erro: O valor deve ser maior que zero!')


valor_produto = solicitar_valor('Valor do produto: R$ ')
imposto = solicitar_valor('Imposto (%): ')

valor_reajustado = somar_imposto(valor_produto, imposto)
print(f'\nValor original: R$ {valor_produto:.2f}\nValor com imposto aplicado: R$ {valor_reajustado:.2f}')

"""
🧠 EXERCÍCIO DO DIA 💭 - DESAFIO

5️⃣ Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação
de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e
passar estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor
ao programa que a chamou.

O programa deverá então exibir o valor a ser pago na tela. Após a execução, o programa deverá voltar a pedir
outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação.
Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o
valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma:

- Para pagamentos sem atraso, cobrar o valor da prestação.
- Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.

"""


def valor_pagamento(_valor_prestacao, _dias_atraso, _taxa_multa, _taxa_juros):
    total_juros_atraso = valor_multa = 0

    if _dias_atraso > 0:
        total_juros_atraso = (_valor_prestacao * _taxa_juros) * _dias_atraso
        valor_multa = (_valor_prestacao * _taxa_multa)

    return {
        VALOR_A_PAGAR: _valor_prestacao + total_juros_atraso + valor_multa,
        VALOR_MULTA: valor_multa,
        VALOR_TOTAL_JUROS: total_juros_atraso
    }


def exibir_relatorio(titulo, cabecalhos, conteudo):
    TAMANHO_MAX_CABECALHO = max(map(lambda _cabecalho: len(_cabecalho), cabecalhos))
    TAMANHO_MAX_VALOR = max(map(lambda valor_linha: max(map(
        lambda valor_coluna: len(f'{valor_coluna:.2f}'), valor_linha)), conteudo))

    print(f'{f"{titulo}":^{TAMANHO_MAX_CABECALHO * len(cabecalhos)}}\n')

    for cabecalho in cabecalhos:
        print(f'{cabecalho:^{TAMANHO_MAX_CABECALHO}}', end='')

    print()

    for linha in conteudo:
        for coluna in linha:
            valor = f'{f"{coluna:.2f}":>{TAMANHO_MAX_VALOR}}'
            print(f'{valor:^{TAMANHO_MAX_CABECALHO}}', end='')
        print()

    print(f'\nTOTAL DE PRESTAÇÕES: {len(conteudo)}\t\t\t'
          f'TOTAL A PAGAR: R$ {sum([linha[-1] for linha in conteudo]):.2f}')


TAXA_MULTA, TAXA_JUROS = 0.03, 0.001
VALOR_A_PAGAR, VALOR_MULTA, VALOR_TOTAL_JUROS = "TOTAL_A_PAGAR", "VALOR_MULTA", "VALOR_TOTAL_JUROS"

relatorio = []

while True:
    while True:
        try:
            valor_prestacao = float(input('\nValor da prestação: R$ ').strip())
        except ValueError:
            print('Erro: Você não informou um valor!')
        else:
            break

    if valor_prestacao == 0:
        break

    while True:
        try:
            dias_atraso = int(input('Dias de atraso: ').strip())
        except ValueError:
            print('Erro: Você não informou um valor!')
        else:
            break

    conta = valor_pagamento(valor_prestacao, dias_atraso, TAXA_MULTA, TAXA_JUROS)

    relatorio.append([valor_prestacao, dias_atraso,
                      conta.get(VALOR_TOTAL_JUROS), conta.get(VALOR_MULTA), conta.get(VALOR_A_PAGAR)])


exibir_relatorio('PRESTAÇÕES', ["VALOR DA PRESTAÇÃO (R$)", "DIAS EM ATRASO", "JUROS POR ATRASO (R$)",
                                "MULTA POR ATRASO (R$)", "VALOR A PAGAR (R$)"], relatorio)

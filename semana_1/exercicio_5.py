"""
🧠 EXERCÍCIO DO DIA 💭 - DESAFIO

5️⃣ Faça um Programa que pergunte o quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o
Imposto de Renda, 8% para o INSS e 5% para o sindicato.

O programa deve nos informar:

A. salário bruto.
B. quanto pagou ao INSS.
C. quanto pagou ao sindicato.
D. o salário líquido.

Calcule os descontos e o salário líquido, conforme a tabela abaixo:

+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$

Obs.: Salário Bruto - Descontos = Salário Líquido.

"""


def calcular_salario_liquido(valor_hora, total_horas_trabalhadas):
    DESCONTOS = {
        'IR': 0.11,
        'INSS': 0.08,
        'SINDICATO': 0.05
    }

    RESULT = {'Salário bruto': valor_hora * total_horas_trabalhadas}

    for descricao, taxa in DESCONTOS.items():
        RESULT[f'- {descricao} ({taxa * 100}%)'] = RESULT.get('Salário bruto') * taxa

    RESULT['Salário líquido'] = RESULT.get('Salário bruto') - sum(list(RESULT.values())[1:])

    print('\n' + '\n'.join([f'{info}: R$ {valor:.2f}' for info, valor in RESULT.items()]))


calcular_salario_liquido(float(input('Valor da hora: R$ ').strip()),
                         float(input('Total de horas trabalhadas: ').strip()))

"""
🧠 EXERCÍCIO DO DIA 💭

3️⃣ Suponha que uma pessoa possa se aposentar pelo INSS caso atenda alguma das situações abaixo:
• É do gênero masculino, possui pelo menos 65 anos e pelo menos 10 anos de contribuição.
• É do gênero masculino, possui pelo menos 63 anos e pelo menos 15 anos de contribuição.
• É do gênero feminino, possui pelo menos 63 anos e pelo menos 10 anos de contribuição.
• É do gênero feminino, possui pelo menos 61 anos e pelo menos 15 anos de contribuição.

Crie um programa que leia um caractere (‘M’ ou ‘F’), que representa o gênero de um indivíduo,
e dois inteiros, que representam a idade e o tempo de contribuição. O programa deverá então imprimir
“Aposentável” se o indivíduo atender uma das situações acima.
Caso contrário, o programa deverá imprimir “Não Aposentável”.
"""


def consultar_aposentadoria(_sexo, _idade, _tempo_contribuicao):
    regras = {
        '15': {'M': 63, 'F': 61},
        '10': {'M': 65, 'F': 63},
        None: {}
    }

    idade_min = regras['15' if _tempo_contribuicao >= 15 else '10' if _tempo_contribuicao >= 10 else None].\
        get(_sexo.upper())

    return 'STATUS: NÃO APONSENTÁVEL' if idade_min is None or _idade < idade_min else 'STATUS: APOSENTÁVEL'


while True:
    try:
        idade = int(input('Idade do contribuinte: ').strip())
    except ValueError:
        print('Dado inválido. Tente novamente!')
    else:
        break

while True:
    sexo = input('Sexo [M / F]: ').strip().upper()
    if sexo in ['M', 'F']:
        break
    print('Dado inválido. Tente novamente!')

while True:
    try:
        tempo_contribuicao = float(input('Tempo de contribuiçao (em anos): ').strip())
    except ValueError:
        print('Dado inválido. Tente novamente!')
    else:
        break

print(f'\n{consultar_aposentadoria(sexo, idade, tempo_contribuicao)}')

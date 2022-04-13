"""
🧠 EXERCÍCIO DO DIA 💭

4️⃣ Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
• Para homens: (72.7h) - 58
• Para mulheres: (62.1h) - 44.7

"""


def calcular_peso_ideal(_sexo, _altura):
    return ((_altura * 72.7) - 58) if _sexo == 'M' else ((_altura * 62.1) - 44.7)


print(f'\n{" CÁLCULO DE PESO IDEAL ":-^50}')

ALTURA_MIN = 1.3

while True:
    sexo = input('Sexo [M / F]: ').strip().upper()

    if sexo in ['M', 'F']:
        break

    print('Erro: Sexo inválido! Informe apenas M ou F.')


while True:
    try:
        altura = float(input('Altura (em metros): ').strip())
    except ValueError:
        print('Erro: Informe um valor para a altura!')
    else:
        break


if altura >= ALTURA_MIN:
    peso_ideal = calcular_peso_ideal(sexo, altura)
    print(f'\nConsiderado a sua altura e o seu sexo, o seu peso ideal é: {peso_ideal:.1f}kg.')
else:
    print(f'\nA altura mínima para o cálculo é de {ALTURA_MIN}m.')

"""
🧠 EXERCÍCIO DO DIA 💭

3️⃣ Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo,
o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos
duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um
valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal
para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para
novos valores de entrada todas as vezes que desejar.

"""

import re


def converter_horario(horas, minutos):
    periodo_dia = "PM" if 24 > horas >= 12 else "AM"

    horas = f'{12 if horas == 0 else horas if horas < 13 else horas - 12}'.zfill(2)
    minutos = f'{minutos}'.zfill(2)

    return f'{horas}:{minutos} {periodo_dia}'


print('\n' + 'CONVERSOR DE HORÁRIO - FORMATO DE 24 HORAS PARA 12'.center(100), end='\n' * 2)

while True:
    horario = input('Infome um horário (formato hh:mm): ').strip()

    if re.match(r'^([0-1]?\d|2[0-3]):[0-5]\d$', horario):

        print(f'=> {converter_horario(*map(int, horario.split(":")))}', end='\n' * 2)

        continuar = None
        while continuar not in ['S', 'N']:
            continuar = input('* Deseja continuar? [S / N]: ').strip().upper()

        print()

        if continuar == 'N':
            break

        continue

    print('\033[1;31mErro: Formato inválido. Tente novamente!\033[m')

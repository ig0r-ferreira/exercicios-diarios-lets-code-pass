"""
🧠 EXERCÍCIO DO DIA 💭

4️⃣ Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são
eliminadas. A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome
do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua
média, conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as
notas restantes). As notas não são informadas ordenadas. Um exemplo de saída do programa deve ser conforme
o exemplo abaixo:

Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04

"""


def solicitar_nota(msg=''):
    while True:
        try:
            nota = float(input(msg).strip())
        except ValueError:
            print('\033[1;31mErro: Você não informou uma nota!\033[m')
        else:
            if 10 >= nota >= 0:
                return nota
            print('\033[1;31mErro: A nota não deve ser menor que ZERO ou maior que DEZ!\033[m')


nome = input('Nome do atleta: ').strip().upper()
notas = [solicitar_nota(f'{i}ª nota: ') for i in range(1, 8)]
media = sum(sorted(notas)[1:-1]) / (len(notas) - 2)

print(f'\nResultado final:\n'
      f'- Atetla: {nome}\n'
      f'- Melhor nota: {max(notas):.2f}\n'
      f'- Pior nota: {min(notas):.2f}\n'
      f'- Média: {media:.2f}')

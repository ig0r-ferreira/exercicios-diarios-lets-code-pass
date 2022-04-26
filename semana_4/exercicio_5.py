"""
🧠 EXERCÍCIO DO DIA 💭 - DESAFIO

5️⃣ Considere a seguinte variação do problema das Torres de Hanói. O objetivo continua sendo mover os n discos do
pino A para o pino C com as restrições: (i) apenas o disco do topo de um pino pode ser movido e (ii) nunca um disco
de diâmetro maior pode ficar sobre um disco de diâmetro menor. Agora adicionamos uma nova restrição: (iii) não é
possível mover um disco diretamente do pino A para o pino C (ou de C para A). Ou seja, para mover um disco de A para
C (ou de C para A), o disco precisa primeiro ser movido para o pino B. Escreva um algoritmo que gere a solução para
este novo problema. A seguinte função deve ser implementada:

hanoi (n , inicial , final , auxiliar )

"""


def hanoi(n, inicial, final, auxiliar):
    if n == 1:
        print(f'Mova o disco {n} de {inicial} para {auxiliar}')
        print(f'Mova o disco {n} de {auxiliar} para {final}')
        return
    hanoi(n - 1, inicial, final, auxiliar)
    print(f'Mova o disco {n} de {inicial} para {auxiliar}')
    hanoi(n - 1, final, inicial, auxiliar)
    print(f'Mova o disco {n} de {auxiliar} para {final}')
    hanoi(n - 1, inicial, final, auxiliar)


while True:
    try:
        quant_discos = int(input('Informe a quantidade de discos: ').strip())
    except ValueError:
        print('\033[1;31mErro: Você não informou um número. Tente novamente!\033[m')
    else:
        if quant_discos > 0:
            break

        print('\033[1;31mErro: Informe um valor maior que zero!\033[m')

print()
hanoi(quant_discos, 'A', 'C', 'B')

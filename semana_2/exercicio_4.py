"""
🧠 EXERCÍCIO DO DIA 💭

4️⃣ Faça um programa que leia duas palavras e verifique se uma delas é subsequência da outra, ou seja,
a primeira pode ser obtida por meio da remoção de letras da segunda.
A ordem das letras não pode ser alterada.

Exemplo de entrada:
moda
moradia
Impressão esperada:
moda é uma subsequência de moradia

Exemplo de entrada:
cereja
cerveja
Impressão esperada:
cereja é uma subsequência de cerveja

Exemplo de entrada:
 teste
 triste
Impressão esperada:
teste não é uma subsequência de triste

"""

p1 = input('1ª palavra: ').strip().lower()
p2 = input('2ª palavra: ').strip().lower()

caracteres_p1 = {c: p1.count(c) for c in p1}

if all([p2.count(c) > 0 and p2.count(c) >= total_c for c, total_c in caracteres_p1.items()]):
    print(f'\n{p1} é uma subsequência de {p2}.')
else:
    print(f'\n{p1} não é uma subsequência de {p2}.')

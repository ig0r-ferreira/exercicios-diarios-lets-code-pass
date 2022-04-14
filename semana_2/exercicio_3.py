"""
🧠 EXERCÍCIO DO DIA 💭

3️⃣ Escreva um programa que leia duas palavras e determine se a segunda é um anagrama da primeira.
Uma palavra é um anagrama de outra se todas as letras de uma ocorrem na outra, em mesmo número,
independente da posição.

Exemplo de entrada:
ROMA
AMOR
Impressão esperada:
Anagramas !

Exemplo de entrada:
REGALIA
ALEGRIA
Impressão esperada:
Anagramas !

Exemplo de entrada:
xzxyxz
yzxyzx
Impressão esperada:
Não são anagramas!

"""

palavra_1 = input('Informe a 1ª palavra: ').strip().lower()
palavra_2 = input('Informe a 2ª palavra: ').strip().lower()

caracteres_palavra_1 = {k: palavra_1.count(k) for k in palavra_1}
caracteres_palavra_2 = {k: palavra_2.count(k) for k in palavra_2}

print(f'\n{"São ANAGRAMAS!" if caracteres_palavra_1 == caracteres_palavra_2 else "Não são ANAGRAMAS!"}')

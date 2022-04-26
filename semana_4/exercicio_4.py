# """
# 🧠 EXERCÍCIO DO DIA 💭
#
# 4️⃣ Crie uma agenda que armazene: código da pessoa, número do telefone e idade.
# Sua agenda deve possibilitar:
#
# (1) – Inserir um contato
# (2) – Remover um contato
# (3) – Editar um contato
# (4) – Buscar um contato pelo Código.
#
# """

import csv
import re


def mostrar_erro(msg):
    print(f'\033[1;31mErro: {msg}\033[m')


def solicitar_codigo(msg):
    while True:
        cod = input(msg).strip().upper()
        if cod == '':
            mostrar_erro('Você não informou um código. Tente novamente!')
            continue

        if buscar_contato(cod) is None:
            raise Exception('Contato não encontrado!')

        break

    return cod


def solicitar_telefone(msg):
    while True:
        telefone = input(msg).strip()
        if re.match(r'^\d{2}\s9?\d{4}-?\d{4}$', telefone):

            telefone = telefone.replace(' ', '').replace('-', '')

            if buscar_contato(telefone):
                raise Exception('Já existe um contato cadastrado com esse telefone!')

            break

        mostrar_erro('Formato inválido. Tente novamente com os formatos: XX 9XXXX-XXXX ou XX XXXX-XXXX!')

    return telefone


def solicitar_idade(msg):
    try:
        idade = int(input(msg).strip())
    except ValueError:
        mostrar_erro('Você não informou um número. Tente novamente!')
    else:
        return idade


def existe_agenda():
    try:
        open('agenda.csv', 'r', newline='')
    except FileNotFoundError:
        return False
    else:
        return True


def criar_agenda():
    with open('agenda.csv', 'a', newline='') as csvfile:
        ids_colunas = ['codigo', 'telefone', 'idade']
        writer = csv.DictWriter(csvfile, fieldnames=ids_colunas)
        writer.writeheader()


def carregar_agenda():
    if not existe_agenda():
        criar_agenda()

    with open('agenda.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)


def salvar_agenda(agenda_atualizada):
    with open('agenda.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['codigo', 'telefone', 'idade'])
        writer.writeheader()
        writer.writerows(agenda_atualizada)


def inserir_contato(**dados):
    agenda = carregar_agenda()

    numeracao = 1 if len(agenda) == 0 else int(agenda[-1].get('codigo')[1:]) + 1
    dados['codigo'] = f'A{str(numeracao).zfill(3)}'

    agenda.append(dados)

    salvar_agenda(agenda)

    return dados.get('codigo')


def buscar_contato(*dados):
    agenda = carregar_agenda()
    result_busca = list(filter(lambda contato: set(dados).intersection(contato.values()), agenda))

    return result_busca[0] if len(result_busca) > 0 else None


def editar_contato(**dados):
    agenda = carregar_agenda()
    contato = buscar_contato(dados.get('codigo'))
    if contato is None:
        raise Exception('Contato não encontrado!')

    contato = agenda[agenda.index(contato)]
    contato.update(dados)

    salvar_agenda(agenda)


def remover_contato(cod):
    agenda = carregar_agenda()
    contato = buscar_contato(cod)
    if contato is None:
        raise Exception('Contato não encontrado!')

    agenda.remove(contato)

    salvar_agenda(agenda)


def listar_contatos(cod=None):
    contatos = carregar_agenda() if cod is None else [buscar_contato(cod)]
    if contatos == [None]:
        raise Exception('Contato não encontrado!')

    print()

    if len(contatos) == 0:
        print('Não há contatos para serem exibidos!')
    else:
        print(f'{"Código":^8}\t{"Telefone":^20}\t{"Idade":^8}')
        for contato in contatos:
            print('{codigo:^8}\t{telefone:^20}\t{idade:^8}'.format(**contato))


def menu():
    return input('(0) - Sair\n'
                 '(1) – Inserir contato\n'
                 '(2) – Remover contato\n'
                 '(3) – Editar contato\n'
                 '(4) – Buscar contato\n'
                 '(5) - Listar contatos\n\n'
                 'Opção: ').strip()


while True:
    print('\n' + ' Agenda '.center(50, '-'), end='\n' * 2)

    match menu():
        case '0':
            break
        case '1':
            try:
                codigo = inserir_contato(telefone=solicitar_telefone('Telefone: '),
                                         idade=solicitar_idade('Idade: '))
            except Exception as erro:
                mostrar_erro(erro)
            else:
                print(f'\nContato registrado! Código: {codigo}')
        case '2':
            try:
                remover_contato(solicitar_codigo('Informe o código do contato: '))
            except Exception as erro:
                mostrar_erro(erro)
            else:
                print(f'\nContato deletado!')
        case '3':
            try:
                editar_contato(codigo=solicitar_codigo('Informe o código do contato: '),
                               telefone=solicitar_telefone('Novo telefone: '),
                               idade=solicitar_idade('Idade atualizada: '))
            except Exception as erro:
                mostrar_erro(erro)
            else:
                print('\nDados atualizados com sucesso!')
        case '4':
            try:
                listar_contatos(solicitar_codigo('Informe o código do contato: '))
            except Exception as erro:
                mostrar_erro(erro)
        case '5':
            listar_contatos()
        case _:
            mostrar_erro('Opção inválida. Tente novamente!')

lista_livro = []
id_global = 0


def mostra_menu():
    print('Escolha a opção desejada: \n'
          ' 1 - Cadastrar livro \n'
          ' 2 - Consultar Livro(s)\n'
          ' 3 - Remover Livro\n'
          ' 4 - Sair')


def cadastrar_livro(id):
    nome = input('Nome: ')
    autor = input('Autor: ')
    editora = input('Editora')

    item = {
        'ID': id,
        'Nome': nome,
        'Autor': autor,
        'Editora': editora
    }
    lista_livro.append(item)
    print('Cadastrado com sucesso')


"""Consultar livros verifica na lista os livros existentes ou não."""


def consultar_livro():
    while True:
        print('1 - Consultar todos \n'
              '2 - Consultar por ID \n'
              '3 - Consultar por autor \n'
              '4 - Retornar ao menu')
        opcao = input('Digite a opcao desejada: ')

        if opcao == '1':
            for item in lista_livro:
                print(item)
        elif opcao == '2':
            idBusca = int(input('Digite o ID'))

            for livro in lista_livro:
                if livro['ID'] == idBusca:
                    print(livro)
                    break
            else:
                print('Nao encontrado')

        elif opcao == '3':
            autorBusca = input('Digite o nome do autor')

            for livro in lista_livro:
                if livro['Autor'] == autorBusca:
                    print(livro)

        elif opcao == '4':
            print('Retornando...')
            break
        else:
            print('Opcao invalida')


"""Consultar livros na lista, caso ele esteja é removido."""


def remover():
    idRemover = int(input('Digite o ID do livro a ser removido'))

    for livro in lista_livro:
        if livro['ID'] == idRemover:
            lista_livro.remove(livro)
            print('Removido com sucesso!')
            return
    else:
        print('Nao encontrado')


print('Bem vindo a livraria do Ráfaga Matos')
print('-' * 50)
print('-' * 17 + ' MENU PRINCIPAL ' + "-" * 17)

while True:
    mostra_menu()
    opcao = input('Digite: ')
    if opcao == '1':
        id_global += 1
        cadastrar_livro(id_global)
    elif opcao == '2':
        consultar_livro()
    elif opcao == '3':
        remover()
    elif opcao == '4':
        break
    else:
        print('Opcao inválida')

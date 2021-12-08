from time import sleep
usuarios = {}
while True:
    decisao = str(input('Escolha uma opção?\n'
                        '[Inserir]\n'
                        '[Pesquisar]\n'
                        '[Excluir]\n'
                        '[Listar]\n'
                        '[Sair]')).capitalize().strip()
    if decisao == 'Inserir':
        usuLogin = input('Digite o login do usuário:').strip()
        usuNome = input(f'Digite o nome e sobrenome do usuário:').capitalize()
        usuDataNas = input(f'Digite a data de acesso do usuário:')
        ususetor = input(f'Informe o setor do usuário {usuLogin}:')
        usuarios[usuLogin] = [usuNome, usuDataNas, ususetor]
    if decisao == 'Pesquisar':
        pesquisar = input('Digite o Login do usuário:')
        print(f'Dados do usuário :\n'
              f'---------------------\n'
              f'Nome:{usuarios.get(pesquisar)[0]}\n'
              f'Data de acesso:{usuarios.get(pesquisar)[1]}\n'
              f'Setor:{usuarios.get(pesquisar)[2]}')
        print('---------------------')
        print()
        sleep(2)
    if decisao == 'Excluir':
        excluir = input('Digite o login do usuário:')
        del usuarios[excluir]
    if decisao == 'Listar':
        for i in usuarios.keys():
            print('=-'*20)
            print(f'Dados do usuário {i}:\n'
                  f'\n'
                  f'Nome: {usuarios.get(i)[0]}\n'
                  f'Data de acesso: {usuarios.get(i)[1]}\n'
                  f'Setor: {usuarios.get(i)[2]}')
            print('=-'*20)
            sleep(2)
            print()
    if decisao == 'Sair':
        break
print('Sistema finalizado.')
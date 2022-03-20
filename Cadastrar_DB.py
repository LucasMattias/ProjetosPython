from time import sleep
import pymysql
import acesso_bd as ab


conexao = pymysql.connect(host=ab.host, database=ab.database, user=ab.user, password=ab.password, port=ab.port)

def cadastrar_pessoa():
    resp =''
    nome = input('Digite o primeiro nome:').title()
    sobrenome = input('Digite o sobrenome: ').title()
    while True:
        cpf = input(f'Digite o CPF de {nome} {sobrenome}:').replace('.', '').replace('-', '')
        if cpf.isnumeric() and len(cpf) == 11:
            break
        print('CPF inválido!')
    while True:
        telefone = input('Digite o telefone:').replace('(', '').replace(')', '').replace('-', '')
        if telefone.isnumeric() and len(telefone) == 11:
            break
        print('Telefone inválido!')
    cursor = conexao.cursor()
    cursor.execute(f'select * from pessoas where cpf = {cpf}')
    banco_limpo = cursor.fetchall()
    if banco_limpo == ():
        cursor.execute(f'insert into pessoas (nome, sobrenome, cpf, telefone) value ("{nome}", "{sobrenome}", {cpf}, {telefone})')
        conexao.commit()
        print('Salvo com sucesso!')
    elif banco_limpo != ():
        print('Pessoa ja cadastrada!')
    if resp != 'S' and resp != 'N':
        resp = input('Deseja adicionar mais pessoas? [S|N]').upper()
    if resp == 'S':
        cadastrar_pessoa()
        cursor.close()


def excluir_pessoas():
    while True:
        esc = input('Digite o CPF que sera excluido:').replace('.', '').replace('-', '')
        if esc.isnumeric() and len(esc) == 11:
            cursor = conexao.cursor()
            cursor.execute(f'select * from pessoas where cpf = {esc}')
            consulta = cursor.fetchall()
            conexao.commit()
            print(f'Nome: {consulta[0][0]}\n'
                 f'Sobrenome: {consulta[0][1]}\n'
                 f'Cpf: {consulta[0][2]}\n'
                 f'Telefone: {consulta[0][3]}\n')
            confirma_esc = input('Deseja mesmo excluir essa pessoa? [S|N]\n'
                 f'').upper()
            if confirma_esc != 'S' and confirma_esc != 'N':
                print('Comando inválido, tente novamente.')
                pass
            elif confirma_esc == 'S':
                cursor.execute(f'delete from pessoas where cpf = {esc}')
                conexao.commit()
                break
            elif confirma_esc == 'N':
                nova_exclusao = input('Deseja realizar mais alguma consulta? [S|N] ').upper().strip()
                if nova_exclusao[0] != 'S':
                    cursor.close()
                    break


def listar_pessoas():
    sleep(1)
    print(f'\033[1:32m{"Colaboradores":=^60}\033[m')
    cursor = conexao.cursor()
    cursor.execute('select count(nome) from pessoas')
    contador = cursor.fetchall()
    cursor.execute('select * from pessoas')
    pessoas = cursor.fetchall()
    for c in range(1, len(contador) + 1):
        sleep(2)
        print(f'\033[1:31m Colaborador nº {c}\033[m')
        for p in pessoas:
            print(f'Nome: {p[0]}\n'
                  f'Sobrenome: {p[1]}\n'
                  f'CPF: {p[2]}\n'
                  f'Telefone: {p[3]}')
            print('-'*30)
            sleep(3)


print(f'\033[1:34m{" Recursos Humanos ":-^60}\033[m')
sleep(2)
print('')
while True:
    perg = input('-----Seja bem vindo(a)-----\n'
                 'Selecione uma opção:\n'
                 '[1] Adicionar Pessoas.\n'
                 '[2] Excluir Pessoas.\n'
                 '[3] Exibir Pessoas.\n'
                 '[4] Fechar Sistema.\n'
                 ':')
    if perg == '1':
        cadastrar_pessoa()
    elif perg == '2':
        excluir_pessoas()
    elif perg == '3':
        listar_pessoas()
    elif perg == '4':
        break
    else:
        print('Favor, inserir um comando válido!')


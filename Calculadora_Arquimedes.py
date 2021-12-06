from time import sleep
print('|=-=Olá, sou Arquimedes, sua calculadora pessoal!=-=|')
sleep(2)
while True:
    operacao = str(input('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|\n'
                         '|=-=-=-=-Qual operação você deseja realizar?-=-=-=-=|\n'
                         '|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|\n'
                         '|=-=-=-=Digite apenas o número correspondente=-=-=-=|\n'
                         '|                   [1]SOMA                         |\n'
                         '|                   [2]SUBTRAÇÃO                    |\n'
                         '|                   [3]MULTIPLICAÇÃO                |\n'
                         '|                   [4]DIVISÃO                      |\n'
                         ':'))
    if operacao in ('1', '2', '3', '4'):
        num = int(input('Ótimo!\n'
                        'Agora digite o primeiro número que deve ser calculado:'))
        num2 = int(input('Maravilha!\n'
                         'Agora eu preciso do segundo número que deve ser calculado:'))
        print('Um minuto caro usuário, estou calculando sua resposta... Com 2308 anos fica dificil hahaha(cof cof) ...')
        sleep(3)
        if operacao == '1':
            print(f'Eureca! O resultado da sua soma de {num}+{num2} é {num + num2}!')
        elif operacao == '2':
            print(f'Eureca! O resultado da sua subtração de {num}-{num2} é {num - num2}!')
        elif operacao == '3':
            print(f'Eureca! O resultado da sua multiplicação de {num}x{num2} é {num * num2}!')
        elif operacao == '4':
            print(f'Eureca! O resultado da sua divisão de {num}/{num2} é {num / num2}!')
        sleep(3)
        perg = str(input('Posso lhe ser util em mais alguma coisa? [ S / N ]')).upper().strip()
        if perg == 'N':
            print('Sinto que isso é um adeus.')
            break
    else:
        print('Não entendi sua resposta, por favor meu caro usuário(a), digite um número válido')
print('Foi um prazer servir a você, volte sempre que possível!')